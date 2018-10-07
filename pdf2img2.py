from pdf2image import convert_from_path


pages=convert_from_path("alphabets.pdf",300)
i=0
for page in pages:
    page.save('source/out'+str(i)+'.jpg', 'JPEG')
    i+=1
