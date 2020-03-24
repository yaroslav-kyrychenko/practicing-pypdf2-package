import PyPDF2


def add_page_and_rotate(pdf_file):
    with open(pdf_file, "rb") as file:
        reader = PyPDF2.PdfFileReader(file)
        page = reader.getPage(0)
        page.rotateClockwise(90)
        writer = PyPDF2.PdfFileWriter()
        writer.addPage(page)
        with open("rotated.pdf", "wb") as output:
            writer.write(output)


def merge_two_pdfs(pdf_1, pdf_2):
    merger = PyPDF2.PdfFileMerger()
    files_to_merge = [pdf_1, pdf_2]
    for file in files_to_merge:
        merger.append(file)
    merger.write("combined.pdf")


merge_two_pdfs("first.pdf", "second.pdf")
