import os
def rn():
    papka = "папка для дз"
    for count, filename in enumerate(os.listdir(papka)):
        a = f"File {str(count)}.pdf"
        s = f"{papka}/{filename}"
        a = f"{papka}/{a}"
        os.rename(s, a)
