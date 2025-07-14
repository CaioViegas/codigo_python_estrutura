import argparse
from pathlib import Path

def create_structure(base_path: Path) -> None:
    """
    Creates a standard structure for a data science project.

    This function creates a series of folders and files commonly used in a data science
    project. The structure is as follows:

        - data/
            - raw/
            - processed/
            - transformed/
        - models/
        - notebooks/
        - scripts/
        - src/
            - etl/
        - logs/
        - tests/

    The following files are created:

        - README.md
        - requirements.txt
        - .gitignore
        - src/utils.py
        - src/config.py
        - scripts/pipeline.py

    :param base_path: The base path where the structure should be created.
    :type base_path: Path
    """
    folders = [
        'data/raw', 'data/processed', 'data/transformed',
        'configs', 'models', 'notebooks', 'scripts', 'src', 'src/etl',
        'logs', 'tests'
    ]

    files = [
        'README.md', 'requirements.txt', '.gitignore',
        'configs/paths.py', 'src/utils.py', 'scripts/pipeline.py'
    ]

    try:
        for folder in folders:
            folder_path = base_path / folder
            folder_path.mkdir(parents=True, exist_ok=True)
            print(f"Created folder: {folder_path}")

        for file in files:
            file_path = base_path / file
            file_path.parent.mkdir(parents=True, exist_ok=True)
            if not file_path.exists():
                file_path.touch()
                print(f"File created in {file_path}")
            else:
                print(f"File already exists: {file_path}")

    except PermissionError:
        print(f"Permission denied to create the structure in: {base_path}")
    except Exception as e:
        print(f"An error has occurred: {str(e)}")

def main():
    """
    Parses command-line arguments and initiates the creation of a data science project structure.

    This function sets up an argument parser to receive the base path where the project structure
    should be created. It resolves the given path and calls the `create_structure` function
    to generate the necessary folders and files.

    Raises:
        SystemExit: If the arguments are not provided correctly.
    """
    parser = argparse.ArgumentParser(
        description="Creates a default structure for a data science project."
    )
    parser.add_argument(
        "path",
        type=str,
        help="The path where the structure will be created."
    )
    args = parser.parse_args()

    base_path = Path(args.path).resolve()
    create_structure(base_path)

if __name__ == "__main__":
    main()