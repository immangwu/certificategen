import pandas as pd
from PIL import Image, ImageDraw, ImageFont
data = pd.read_excel(r'C:\Users\Immanual mech\Desktop\tools for program\certificates generator\BDE.xlsx')
name_list = data["Name"].tolist()
id=data["Id"].tolist()
for ind,i in enumerate(name_list):
    im = Image.open(r'C:\Users\Immanual mech\Desktop\tools for program\certificates generator\invitation.jpg')
    d = ImageDraw.Draw(im)
    location1 = (600, 1710)
    text_color1 = (0, 137, 209)
    location2 = (600, 5500)
    text_color2 = (100, 137, 209)
    font = ImageFont.truetype("arial.ttf", 250)
    font0 = ImageFont.truetype("arial.ttf", 100)
    d.text(location1, i, fill = text_color1, font = font)
    d.text(location2, 'Id:'+str(id[ind]), fill = text_color2, font = font0)
    im.save("Invitation_" + i + ".pdf")
