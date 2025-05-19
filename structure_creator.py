import os

"""
Este script cria a estrutura inicial de diretórios e arquivos para um projeto de Ciência de Dados.
"""

folders = ['data/raw', 'data/processed', 'data/transformed', 'models', 
           'notebooks', 'scripts', 'src', 'logs', 'tests']

files = ['README.md', 'requirements.txt', '.gitignore', 'src/utils.py', 
         'src/config.py', 'src/etl', 'scripts/pipeline.py']

base_path = str(input("Caminho do diretório: ").strip())
base_path = os.path.normpath(base_path)

try:
    with open('gitignore_template.txt', 'r') as template:
        gitignore_content = template.read()

except FileNotFoundError:
    print("Erro: Arquivo 'gitignore_template.txt' não encontrado.")
    exit()

try:
    for folder in folders:
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        open(os.path.join(folder_path, '.gitkeep'), 'a').close()

    for file in files:
        file_path = os.path.join(base_path, file)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        open(file_path, 'a').close()

        if file.endswith('.gitignore') and os.stat(file_path).st_size == 0:
            with open(file_path, 'w') as f:
                f.write(gitignore_content)

    print("Projeto criado com sucesso em:", base_path)

except PermissionError:
    print(f"Erro: Permissão negada. Não foi possível criar em {base_path}")
    print("Tente:")
    print("1. Executar como administrador")
    print("2. Escolher um diretório diferente")
    
except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")