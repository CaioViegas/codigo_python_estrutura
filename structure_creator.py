import os

folders = ['data/raw', 'data/processed', 'data/transformed', 'models', 
           'notebooks', 'scripts', 'src', 'logs', 'tests']

files = ['README.md', 'requirements.txt', '.gitignore', 'src/utils.py', 
         'src/config.py', 'scripts/pipeline.py']

base_path = str(input("Caminho do diretório: ").strip())

base_path = os.path.normpath(base_path)

try:
    for folder in folders:
        os.makedirs(os.path.join(base_path, folder), exist_ok=True)
    for file in files:
        file_path = os.path.join(base_path, file)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        open(file_path, 'a').close()
    print("Projeto criado com sucesso em:", base_path)
except PermissionError:
    print(f"Erro: Permissão negada. Não foi possível criar em {base_path}")
    print("Tente:")
    print("1. Executar como administrador")
    print("2. Escolher um diretório diferente")
except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")