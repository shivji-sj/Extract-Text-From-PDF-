# Text Extraction form PDF - Text Processing Project
import PyPDF2 as pf


pdf = open(r"your_file_name", "rb")


# 1. Extract all Pages
def all_page(pdf):
    reader = pf.PdfReader(pdf)
    total_pages = len(reader.pages)
    for i in range(0, total_pages):
        page = reader.pages[i]
        text = page.extract_text()
        print(text)

# 2. extract custom page
def custom_page(pdf, page_no=0):
    reader = pf.PdfReader(pdf)

    if page_no == 1 or page_no == 0:
        page_no = page_no
        page = reader.pages[page_no]
        text = page.extract_text()
        print(text)
        
    elif page_no >= 2:
        page_no = page_no
        page = reader.pages[page_no - 1]
        text = page.extract_text()
        print(text)
    else:
        print("Invalid Page Number!")

# custom_page(pdf, 5)

# 3. Custom Page Range 
def custom_page_range(pdf, s_page_no, b_page_no):
    reader = pf.PdfReader(pdf)

    for i in range(s_page_no - 1, b_page_no):
        page = reader.pages[i]
        text = page.extract_text()
        print(text)

# custom_page_range(pdf ,1,8)

# 4. PDF page length
def pdf_length(pdf):
    global total_pages
    reader = pf.PdfReader(pdf)
    print(len(reader.pages))
# pdf_length(pdf)


