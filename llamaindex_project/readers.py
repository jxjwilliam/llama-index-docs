from llama_index.core import SimpleDirectoryReader
from llama_index.core.readers.file.base import BaseReader
from llama_index.readers.file import (
    DocxReader,
    PDFReader,
    FlatReader,
    HTMLTagReader,
    ImageReader,
    IPYNBReader,
    MarkdownReader,
    MboxReader,
    PandasCSVReader,
    PagedCSVReader,
    CSVReader
)

# PDF Reader with `SimpleDirectoryReader`
parser = PDFReader()
file_extractor = {".pdf": parser}
documents = SimpleDirectoryReader(
    "./data", file_extractor=file_extractor
).load_data()

# Docx Reader example
parser = DocxReader()
file_extractor = {".docx": parser}
documents = SimpleDirectoryReader(
    "./data", file_extractor=file_extractor
).load_data()

# Flat Reader example
parser = FlatReader()
file_extractor = {".txt": parser}
documents = SimpleDirectoryReader(
    "./data", file_extractor=file_extractor
).load_data()

# HTML Tag Reader example
parser = HTMLTagReader()
file_extractor = {".html": parser}
documents = SimpleDirectoryReader(
    "./data", file_extractor=file_extractor
).load_data()

# Image Reader example
parser = ImageReader()
file_extractor = {
    ".jpg": parser,
    ".jpeg": parser,
    ".png": parser,
}  # Add other image formats as needed
documents = SimpleDirectoryReader(
    "./data", file_extractor=file_extractor
).load_data()

# IPYNB Reader example
parser = IPYNBReader()
file_extractor = {".ipynb": parser}
documents = SimpleDirectoryReader(
    "./data", file_extractor=file_extractor
).load_data()

# Markdown Reader example
parser = MarkdownReader()
file_extractor = {".md": parser}
documents = SimpleDirectoryReader(
    "./data", file_extractor=file_extractor
).load_data()

# Mbox Reader example
parser = MboxReader()
file_extractor = {".mbox": parser}
documents = SimpleDirectoryReader(
    "./data", file_extractor=file_extractor
).load_data()

# Pandas CSV Reader example
parser = PandasCSVReader()
file_extractor = {".csv": parser}  # Add other CSV formats as needed
documents = SimpleDirectoryReader(
    "./data", file_extractor=file_extractor
).load_data()

# Paged CSV Reader example
parser = PagedCSVReader()
file_extractor = {".csv": parser}  # Add other CSV formats as needed
documents = SimpleDirectoryReader(
    "./data", file_extractor=file_extractor
).load_data()

# CSV Reader example
parser = CSVReader()
file_extractor = {".csv": parser}  # Add other CSV formats as needed
documents = SimpleDirectoryReader(
    "./data", file_extractor=file_extractor
).load_data()
