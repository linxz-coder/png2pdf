from PIL import Image
import os
from reportlab.pdfgen import canvas

def create_pdf_from_images(folder_path, output_pdf_path="output.pdf"):
    # 获取指定文件夹中的所有PNG文件
    images = [f for f in os.listdir(folder_path) if f.endswith('.png')]

    # 按照文件名中的数字进行排序
    images.sort(key=lambda x: int(x.split('图片')[0]))

    # 创建PDF文件
    c = canvas.Canvas(output_pdf_path)

    for i, image_name in enumerate(images):
        image_path = os.path.join(folder_path, image_name)
        img = Image.open(image_path)

        # 获取图片原始尺寸
        width, height = img.size

        # 设置PDF页面大小为图片大小
        c.setPageSize((width, height))

        # 添加图片到PDF
        c.drawImage(image_path, 0, 0, width=width, height=height)

        # 在添加完图片后调用showPage，除了最后一张图片
        if i < len(images) - 1:
            c.showPage()

    c.save()
    return "PDF created successfully."

# 示例使用
# folder_path = "path_to_your_folder" # 替换为您的图片文件夹路径
# create_pdf_from_images(folder_path)
create_pdf_from_images("/Users/lxz/Downloads/pain is strange")
