import fitz  # PyMuPDF

def extract_text_pymupdf(pdf_path, txt_path):
    try:
        # باز کردن فایل PDF
        doc = fitz.open(pdf_path)
        
        with open(txt_path, 'w', encoding='utf-8') as txt_file:
            for page_num, page in enumerate(doc):
                # استخراج متن
                text = page.get_text()
                
                txt_file.write(text)
                txt_file.write(f'\n\n--- پایان صفحه {page_num + 1} ---\n\n')
                
        print(f"✅ متن با موفقیت استخراج شد و در فایل '{txt_path}' ذخیره گردید.")
        
    except Exception as e:
        print(f"❌ خطایی رخ داد: {e}")

# آدرس فایل‌های خود را اینجا قرار دهید (با استفاده از r قبل از آدرس)
input_pdf = r"D:\Amin_Projects\GitHub_Projects\Dataset_Project\PDFs_datas\10.22084_nfag.2023.27615.1548 (1).pdf"
output_txt = r"output.txt"

extract_text_pymupdf(input_pdf, output_txt)