from PyPDF2 import PdfWriter, PdfReader 
import fitz

print("Welcome to PDF TOOLKIT 1.0")
print("-----------------------------------------")

print("What do you want to use.")
print('''
1. Extract Text from a PDF
2. Extract Images
3. Merging PDF files
4. Adding a Stamp/Watermark to a PDF
5. Reduce PDF Size
''')

chc = int(input("Enter your choice : "))

if chc == 1:
    try:
        print("-----------------------------------------")

        d = input("Enter the name of the pdf : ")

        new_file = input("Enter the new name of the file in which you want to keep the text(do not forgot to add .txt) : ")
        print("-----------------------------------------")


        reader = PdfReader(d)

        f = open(new_file,"w")
        for i, page in enumerate(reader.pages):
            f.write(f"\n --- Page {i+1} ---\n")
            f.write(page.extract_text())

        f.close()
        print("Task Complete....")

    except Exception as e:
        print(e)

if chc == 2:
    try:
        print("-----------------------------------------")
        pdf_file = input("Enter the name of Pdf file : ")
        doc = fitz.open(pdf_file)

        count = 0

        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            images = page.get_images(full=True)

            for img_index, img in enumerate(images):
                xref = img[0]
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]

                with open(f"image_{count}.{image_ext}", "wb") as f:
                    f.write(image_bytes)
                count += 1
        print("-----------------------------------------")
        print(f"{count} image(s) extracted from '{pdf_file}' ")
        print("-----------------------------------------")

    except Exception as e:
        print(e)

if chc == 3:
    try:
        merger = PdfWriter()
        pdfs = []
        print("-----------------------------------------")
        n = int(input("How many pdf do you want to merge : "))

        print("-----------------------------------------")
        for i in range(0,n):
            name = input("Enter the name of the pdf : ")
            pdfs.append(name)


        for pdf in pdfs:
            merger.append(pdf)

        merger.write("merged-pdf.pdf")
        merger.close()
        print("Task Completed......")
        print("-----------------------------------------")
    except Exception as e :
        print(e)

if chc == 4:
    try:
        print("-----------------------------------------")
        input_pdf = input("Please enter the name of the PDF file to which you want to add a watermark : ")
        watermark_pdf = input("please enter the name of the stamp pdf : ")
        print("-----------------------------------------")
        output_pdf = "watermarked_output.pdf"

        # Load files
        reader = PdfReader(input_pdf)
        watermark = PdfReader(watermark_pdf)
        writer = PdfWriter()

        watermark_page = watermark.pages[0]

        # Merge watermark on every page
        for page in reader.pages:
            page.merge_page(watermark_page)
            writer.add_page(page)

        # Save output
        with open(output_pdf, "wb") as f:
            writer.write(f)

        print("Watermark added to all pages!")
        print("-----------------------------------------")
    
    except Exception as e:
        print(e)

if chc == 5:
    try:
        print("-----------------------------------------")
        pdfs = input("Enter the name of pdf : ")
        print("-----------------------------------------")
        reader = PdfReader(pdfs)
        writer = PdfWriter()

        for page in reader.pages:
            page.compress_content_streams()  # This is CPU intensive!
            writer.add_page(page)

        with open("reduced.pdf", "wb") as f:
            writer.write(f)
        print("Task completed... \n Reduced pdf saved in the folder named reduced.pdf")
        print("-----------------------------------------")

    except Exception as e :
        print(e)
