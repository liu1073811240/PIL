from PIL import Image, ImageFilter, ImageDraw, ImageFont


image = Image.open("./huge.jpeg")
img1 = image.filter(ImageFilter.BLUR)  # 模糊
img2 = image.filter(ImageFilter.DETAIL)  # 增强饱和度
img3 = image.filter(ImageFilter.CONTOUR)  # 轮廓
img4 = image.filter(ImageFilter.EMBOSS)  # 浮雕

# img1.show()
# img2.show()
# img3.show()
# img4.show()

draw = ImageDraw.Draw(image)
# draw.point(xy=(200, 200), fill="red")
# draw.line(xy=(300, 300, 800, 800), fill="green", width=3)
# draw.rectangle((150, 40, 451, 480), fill=None, outline="red", )

# draw.rectangle((100, 100, 400, 200), fill=None, outline="yellow")
# draw.ellipse((100, 100, 400, 200), fill="red", outline="yellow")  # 画椭圆

# draw.rectangle((400, 400, 600, 600), fill=None)
# draw.arc((400, 400, 600, 600), start=0, end=30, fill="blue")  # 画圆弧
# draw.chord((200, 200, 400, 400), start=0, end=270, outline="red")  # 画和弦
# print(image.size)

font_path = "./msgothic.ttc"
font = ImageFont.truetype(font_path, size=60)
draw.text(xy=(10, 10), text="这是中文字体", fill="red", font=font)

image.show()





