from PIL import Image

import os

downloadsf = "C:/Users/juane/Downloads/"
picturedes = "C:/Users/juane/Pictures/imagenes-des/"

if __name__ == "__main__":

    for filename in os.listdir(downloadsf):
        name, extension = os.path.splitext(downloadsf+filename)

        if extension in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(downloadsf+filename)
            picture.save(picturedes+"compressed_"+filename,
                         optimize=True, quality=60)
            os.remove(downloadsf+filename)
            print(name+"+"+extension)

        if extension in [".xlsx", ".docx", ".pptx"]:
            office = "C:/Users/juane/Desktop/trabajos-office/"
            os.rename(downloadsf+filename, office+filename)
            
        if extension in [".pdf", ".txt", ".zip", ".rar", ".epub"]:
            pdf = "C:/Users/juane/Desktop/pdf-txt/"
            os.rename(downloadsf+filename, pdf+filename)
