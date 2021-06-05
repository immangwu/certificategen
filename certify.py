import pandas as pd
from PIL import Image, ImageDraw, ImageFont
data = pd.read_excel(r'C:\Users\Immanual mech\Desktop\Events\ip seminar\certificategen-main\BDE.xlsx')
name_list = data["Name"].tolist()
id=data["Id"].tolist()
for ind,i in enumerate(name_list):
    i=i.title()
    im = Image.open(r'C:\Users\Immanual mech\Desktop\Events\ip seminar\certificategen-main\certi.jpg')
    image_width = im.width;
    image_height = im.height;
    d = ImageDraw.Draw(im)
    
    
    text_color1 = (230, 230, 0)#(0, 137, 209)
    location2 = (480, 880)
    text_color2 = (200, 137, 209)
    font = ImageFont.truetype(r'C:\Users\Immanual mech\Desktop\Events\ip seminar\certificategen-main\edwardian-script-itc\ITCEDSCR.ttf', 70)
    #font = ImageFont.truetype("arial.ttf", 50)
    font0 = ImageFont.truetype("arial.ttf", 30)
    text_width, _ = d.textsize(i, font = font)
    location1 = ((image_width - text_width) / 2, 550) #350
    d.text(location1, i, fill = text_color1, font = font,stroke_width=1)
    d.text(location2, 'Certificate Id :'+str(id[ind]), fill = text_color2, font = font0)
    im.save("Certificate_" + i + ".pdf")
    print(i)
