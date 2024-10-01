'''
function:读取不同来源与不同格式的文件

input:文件路径
output:文件内容

逗号分隔值(CSV) 文件是一种使用逗号分隔值的定界文本文件。
文件的每一行是一个数据记录。每个记录由一个或多个字段组成，字段之间用逗号分隔
'''
from langchain.document_loaders import PyPDFLoader, Docx2txtLoader, UnstructuredFileLoader, TextLoader

from langchain.document_loaders import TextLoader
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.document_loaders import UnstructuredHTMLLoader

class DocumentReader:
    def __init__(self,file_path):

        self.legal_suffix = ['doc','docx','pdf','csv','txt','md','html']

        # 文件格式判断
        if file_path.split('.')[-1] in self.legal_suffix:
            self.file_path = file_path
            self.file_type = file_path.split('.')[-1]
        else:
            raise Exception('文件格式不支持')
        
        if self.file_type == 'doc':
            self.content = self.read_doc()
        elif self.file_type == 'docx':
            self.content = self.read_docx()
        elif self.file_type == 'pdf':
            self.content = self.read_pdf()
        elif self.file_type == 'csv':
            self.content = self.read_csv()
        elif self.file_type == 'txt' or self.file_type == 'md':
            self.content = self.read_txt()
        elif self.file_type == 'html':
            self.content = self.read_html()
    # 读取文件内容
    def read_doc(self):

        # doc格式 需要转换成docx格式
        
        return self.read_docx()
    
    def read_docx(self):

        loader = Docx2txtLoader(file_path=self.file_path)
        return loader.load_and_split('/n')
    def read_pdf(self):

        loader = PyPDFLoader(file_path=self.file_path) 
        return loader.load_and_split()
    def read_txt(self):
        
        loader = TextLoader(file_path=self.file_path)
        return loader.load()

    def read_csv(self):

        loader = CSVLoader(file_path=self.file_path)
        return loader.load()
    
    def read_html(self):

        loader = UnstructuredHTMLLoader(file_path=self.file_path)
        return loader.load()

if __name__ == '__main__':


    # 相对路径？
    # file_path = '/Users/dummy/CodeSpace/GIT/rag/example/data/2024考研英语阅读预测讲义.pdf'
    # file_path = 'example/data/review.md'
    # file_path = 'example/data/2024考研英语阅读预测讲义.doc'
    file_path = 'example/data/01.docx'
    reader = DocumentReader(file_path)
    print(reader.content)
    