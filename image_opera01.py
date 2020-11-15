from PIL import Image
import numpy as np

path1 = r"D:\PycharmProjects\2020-07-25-PIL\directory\jinchen.jpeg"
path2 = r"directory/jinchen.jpeg"
img = Image.open(path2)
print(img)
# img.show()

w, h = img.size
print(img.size)

# 图像转numpy数组
a = np.array(img)
print(a)
print(a.shape)

# numpy数组转图像
b = Image.fromarray(a)
print(b)
# b.show()

# 统计图片的像素直方图，统计每个像素值出现的次数
his = img.histogram()
print(his)
print(len(his))

# 查看指定坐标位置的像素点的RGB值
print(img.size)
pixes = img.getpixel((120, 80))
print(pixes)

# 查看图像的模式类型
bands = img.getbands()
print(bands)

# 按指定角度旋转图像，返回旋转后的图像
# img = img.rotate(45)
# img.show()

# 按指定坐标位置裁剪图片
img2 = img.crop((100, 100, 2000, 2000))
# img2.show()
print(img2.size)

# 使用切片的方法裁剪图片
print(np.array(img)[100:600, 500:1000, :].shape)  # h, w, c        
img2 = Image.fromarray(np.array(img)[100:600, 500:1000, :])  # h, w, c
# img2.show()

# 按指定尺寸大小缩放图像，返回缩放后的图像
x = img.resize((800, 800))  # 图像会变形
# x.show()

# thumbnail按最大边等比例缩放，没有返回值
# 相当于直接把图片缩放
img.thumbnail((8000, 8000))
# img.show()

# 将图像转成灰度图，单通道
img = img.convert("L")
bands = img.getbands()
print(bands)
# img.show()

# 将图像转成RGB图，三通道
img = img.convert("RGB")
# img.show()
print(np.array(img).shape)

# 将一张图片按指定位置粘贴到另一张图片上
img.paste(Image.open("huge.jpeg"), (10, 10))
# img.show()

# 保存图像
# img.save("./directory/1.jpg")

# 生成一张空白图片
image = Image.new("RGB", (100, 100), (255, 255, 255))
image.show()


