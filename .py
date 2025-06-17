from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


# 解析PDF，切成chunk片段
pdf_loader=PyPDFLoader('E:\RAG_test\风洞试验规范.pdf',extract_images=True)   # 使用OCR解析pdf中图片里面的文字
chunks=pdf_loader.load_and_split(text_splitter=RecursiveCharacterTextSplitter(chunk_size=100,chunk_overlap=10))


