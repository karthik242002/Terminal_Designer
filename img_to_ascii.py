from Designer.General import *
# also you can import >>> from Designer.General import img_to_ascii
# >>> import Designer
# >>> Designer.General.img_to_ascii("path")

a = img_to_ascii("sample.jpg")

with open("sample.txt",'w') as f:
    f.writelines(a)
f.close()