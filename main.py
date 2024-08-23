from glob import glob
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from dotenv import load_dotenv
from llama_index.readers.file import MarkdownReader

load_dotenv()

# Specify the directory path
directory_path = "./data"
parser = MarkdownReader()
file_extractor = { ".md": parser }
exclude_path = glob("data/imgs/**/*")

documents = SimpleDirectoryReader(
    directory_path,
    recursive=True,
    exclude=exclude_path,
    exclude_hidden=True,
    file_extractor=file_extractor,
).load_data()


print(f"Number of documents loaded: {len(documents)}")

# Print the text of the first document (if any documents were loaded)
if documents:
    print("\nText of the first Markdown document:")
    print(documents[0].text[:500] + "..." if len(documents[0].text) > 500 else documents[0].text)
else:
    print("No Markdown documents were loaded.")

# Print all file paths
# print("\nAll Markdown file paths:")
# for doc in documents:
#     print(doc.metadata['file_path'])


index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()

response = query_engine.query("What is llama-index?")

print(response)