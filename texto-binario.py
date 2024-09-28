# 100SECURITY
# Converter Textos e Arquivos <> Binário
# Por: Marcos Henrique
# Site: www.100security.com.br

import os
from colorama import Fore, Style

# Limpar a Tela
def clear_screen():
    if os.name == 'nt':  # Se for Windows
        os.system('cls')
    else:  # Se for Linux ou macOS
        os.system('clear')
        
clear_screen()

# Inicializa o Colorama
from colorama import init
init(autoreset=True)

# Banner
projeto = f"{Style.BRIGHT}{Fore.YELLOW}# - - - - - - - - 100SECURITY - - - - - - - - #\n"
titulo = f"{Style.BRIGHT}{Fore.GREEN}Converter Textos e Arquivos <> Binário"
github = f"{Style.BRIGHT}{Fore.WHITE}GitHub: {Fore.WHITE}github.com/100security/{Style.BRIGHT}{Fore.LIGHTCYAN_EX}texto-binario"
instagram = f"{Style.BRIGHT}{Fore.WHITE}Instagram: {Fore.WHITE}{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}@100security"

# Exibe o texto com as cores e com uma nova linha entre eles
print(f"{projeto}\n{titulo}\n{github}\n{instagram}")

# Função para converter texto em binário
def text_to_binary(text):
    binary_values = ' '.join(format(ord(char), '08b') for char in text)
    return binary_values

# Função para converter binário para texto
def binary_to_text(binary_values):
    binary_values = binary_values.split()  # Divide os bits
    text = ''.join(chr(int(b, 2)) for b in binary_values)
    return text

# Função para converter arquivo de texto em binário
def text_file_to_binary(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text_to_binary(text)
    except FileNotFoundError:
        print(f"{Style.BRIGHT}{Fore.RED}Arquivo não encontrado. Verifique o caminho do arquivo.")

# Função para converter binário de um arquivo para texto
def binary_file_to_text(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            binary_values = file.read()
        return binary_to_text(binary_values)
    except FileNotFoundError:
        print(f"{Style.BRIGHT}{Fore.RED}Arquivo não encontrado. Verifique o caminho do arquivo.")
    except ValueError:
        print(f"{Style.BRIGHT}{Fore.RED}Erro na conversão. Verifique o conteúdo do arquivo.")

# Função para converter arquivos binários em código binário (com representação binária)
def file_to_binary(file_path):
    try:
        with open(file_path, 'rb') as file:
            binary_data = file.read()
        return ' '.join(format(byte, '08b') for byte in binary_data)
    except FileNotFoundError:
        print(f"{Style.BRIGHT}{Fore.RED}Arquivo não encontrado. Verifique o caminho do arquivo.")

# Função para converter binário de um arquivo para arquivo binário real
def binary_file_to_binary(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            binary_data = file.read().split()

        binary_bytes = bytearray([int(b, 2) for b in binary_data])
        
        with open(output_file, 'wb') as file:
            file.write(binary_bytes)
        
        print(f"{Style.BRIGHT}{Fore.LIGHTGREEN_EX}Arquivo {output_file} criado com sucesso!")
    except FileNotFoundError:
        print(f"{Style.BRIGHT}{Fore.RED}Arquivo {input_file} não encontrado.")
    except ValueError:
        print(f"{Style.BRIGHT}{Fore.RED}Erro na conversão de binário para arquivo. Verifique o conteúdo.")

# Função para salvar o conteúdo em um arquivo
def salvar_em_arquivo(file_name, content):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"{Style.BRIGHT}{Fore.LIGHTGREEN_EX}Resultado salvo em {file_name}")

# Função para exibir o menu
def exibir_menu():
    print(f"\n{Style.BRIGHT}{Fore.RED}# - - - - - - - - - M E N U - - - - - - - - - #\n")
    print(f"{Style.BRIGHT}{Fore.WHITE}1 {Style.NORMAL}{Fore.WHITE}- Converter {Style.BRIGHT}{Fore.LIGHTCYAN_EX}Texto {Fore.WHITE}para {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}Binário")
    print(f"{Style.BRIGHT}{Fore.WHITE}2 {Style.NORMAL}{Fore.WHITE}- Converter {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}Binário {Fore.WHITE}para {Fore.LIGHTCYAN_EX}Texto")
    print(f"{Style.BRIGHT}{Fore.WHITE}3 {Style.NORMAL}{Fore.WHITE}- Converter {Style.BRIGHT}{Fore.LIGHTCYAN_EX}texto.txt {Fore.WHITE}para {Fore.LIGHTYELLOW_EX}Binário")
    print(f"{Style.BRIGHT}{Fore.WHITE}4 {Style.NORMAL}{Fore.WHITE}- Converter {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}binario.txt {Fore.WHITE}para {Fore.LIGHTCYAN_EX}Texto")
    print(f"{Style.BRIGHT}{Fore.WHITE}5 {Style.NORMAL}{Fore.WHITE}- Converter {Style.BRIGHT}{Fore.LIGHTCYAN_EX}Arquivos {Fore.WHITE}para {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}Binário")
    print(f"{Style.BRIGHT}{Fore.WHITE}6 {Style.NORMAL}{Fore.WHITE}- Converter {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}Binário {Fore.WHITE}para {Fore.LIGHTCYAN_EX}Arquivo")
    print(f"{Style.BRIGHT}{Fore.WHITE}7 {Style.NORMAL}{Fore.WHITE}- {Style.BRIGHT}{Fore.LIGHTRED_EX}Sair\n")

# Função principal
def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            texto = input("Digite o Texto a ser convertido para Binário: ")
            binary_result = text_to_binary(texto)
            salvar_em_arquivo('binario.txt', binary_result)
            print(f"Texto original: {Style.BRIGHT}{Fore.LIGHTCYAN_EX}{texto}")
            print(f"Conversão para Binário: {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}{binary_result}")
        
        elif opcao == '2':
            binary_input = input("Digite os valores binários separados por espaço: ")
            try:
                texto_result = binary_to_text(binary_input)
                salvar_em_arquivo('texto.txt', texto_result)
                print(f"Valores Binários: {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}{binary_input}")
                print(f"Conversão para Texto: {Style.BRIGHT}{Fore.LIGHTCYAN_EX}{texto_result}")
            except ValueError:
                print(f"{Style.BRIGHT}{Fore.RED}Entrada inválida. Por favor, insira apenas valores binários separados por espaços.")
        
        elif opcao == '3':
            file_path = input("Digite o nome do arquivo de texto (.txt): ")
            binary_result = text_file_to_binary(file_path)
            if binary_result:
                salvar_em_arquivo('binario.txt', binary_result)
                print(f"Conversão de {file_path} para Binário: {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}{binary_result}")
        
        elif opcao == '4':
            file_path = input("Digite o nome do arquivo de binário (.txt): ")
            texto_result = binary_file_to_text(file_path)
            if texto_result:
                salvar_em_arquivo('texto.txt', texto_result)
                print(f"Conversão de {file_path} para Texto: {Style.BRIGHT}{Fore.LIGHTCYAN_EX}{texto_result}")
        
        elif opcao == '5':
            file_path = input("Digite o nome do arquivo (ex: imagem.png, arquivo.pdf): ")
            binary_result = file_to_binary(file_path)
            if binary_result:
                salvar_em_arquivo('binario.txt', binary_result)
                print(f"Conversão de {file_path} para Binário: {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}{binary_result}")
        
        elif opcao == '6':
            input_file = input("Digite o nome do arquivo binário (ex: binario.txt): ")
            output_file = input("Digite o nome do arquivo de saída (ex: imagem.png, arquivo.pdf): ")
            binary_file_to_binary(input_file, output_file)

        elif opcao == '7':
            print(f"{Style.BRIGHT}{Fore.LIGHTRED_EX}Saindo...")
            break

        else:
            print(f"{Style.BRIGHT}{Fore.RED}Opção inválida. Tente novamente.")

# Executar o programa
if __name__ == "__main__":
    main()
