import os
from glob import glob
from llama_index.core import SimpleDirectoryReader
from llama_index.core.readers.file.base import BaseReader
from dotenv import load_dotenv

load_dotenv()

markdown_files = glob("data/**/*.md")
exclude_path = glob("data/imgs")

def collect_md_files():
    all_files = []
    for root, dirs, files in os.walk("data"):
        for file in files:
            if file.endswith(".md"):
                all_files.append(os.path.join(root, file))
    return all_files


def load_md_files(file_path):
    if file_path.endswith('.md'):
        with open(file_path, 'r') as f:
            return [{"text": f.read(), "extra_info": {"file_path": file_path}}]
        return []
    


documents = SimpleDirectoryReader(
    input_files=markdown_files,
    recursive=True,
    exclude_hidden=True, # .git, .vscode, .editorconfig
    exclude=exclude_path,
    ).load_data()

if documents:
    print(documents[0].text)