#! /usr/bin/python3
# copyright 2024 CHUA某人，版权所有。
# bak2zip ——一键备份你的所有重要文件，让你不再为丢失文件而烦恼！
# 用法：import bak2zip;bak2zip.bak('指定的目录')

import os
import zipfile
from pathlib import Path


def bak(folder):
    """
    功能：将源文件夹中的全部内容备份到zip压缩包中
    参数：文件夹路径
    """
    folder = os.path.abspath(folder)  # 确保源文件夹为绝对路径

    # 根据已存在的zip压缩包，找出这段代码应该使用的zip压缩包名
    num = 1
    while 1:
        zip_name = os.path.basename(folder) + '_' + str(num) + '.zip'
        if not os.path.exists(zip_name):
            break
        num += 1

    # 创建新zip压缩包
    print(f'正在备份{folder}到{zip_name}中，请稍后……')
    bak_zip = zipfile.ZipFile(Path(folder) / zip_name, 'w')

    # 遍历整个文件夹，并把每个文件夹中的文件添加进zip压缩包
    for foldername, subfolder, filenames in os.walk(folder):
        print(f'正在把文件夹{foldername}中文件添加进{zip_name}中，请稍后……')

        # 将当前文件夹添加进zip压缩包中
        bak_zip.write(foldername, compress_type=zipfile.ZIP_DEFLATED)

        # 向zip压缩包添加该文件夹下所有文件
        for filename in filenames:
            new_base = os.path.basename(folder) + '_'
            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue
            bak_zip.write(os.path.join(foldername, filename), compress_type=zipfile.ZIP_DEFLATED)

    bak_zip.close()
    print(f'备份完成！备份文件在{Path(folder) / zip_name}处！')
