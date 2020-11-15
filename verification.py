from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

#随机字母
def randChar():
    a = chr(random.randint(65, 90))
    b = chr(random.randint(97, 122))
    c = str(random.randint(0, 9))
    return random.choice([a, b, c])

# 背景颜色1
def ranColor1():
    return (random.randint(65, 255),
            random.randint(65, 255),
            random.randint(65, 255))
# 前景颜色2
def ranColor2():
    return (random.randint(32, 127),
            random.randint(32, 127),
            random.randint(32, 127))

# 240*60
width = 240
height = 60
image = Image.new("RGB", (width, height), (255, 255, 255))
# 创建字体对象
font = ImageFont.truetype("simsun.ttc", 40)
# 创建draw对象
draw = ImageDraw.Draw(image)

for k in range(10):
# 填充像素
    for i in range(width):
        for j in range(height):
            draw.point((i, j), fill=ranColor1())

    # image.show()
    # 填充文字
    for i in range(4):
        draw.text((60*i+10, 10), randChar(), font=font, fill=ranColor2())

    image = image.filter(ImageFilter.BLUR)
    # image.show()
    image.save("./directory/{0}.jpg".format(k+1))


