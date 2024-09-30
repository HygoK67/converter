import os
import shutil

# 设定源文件夹和目标文件夹路径
converted = './converted'  # 替换为你的源文件夹路径
destination_folder = './target_files'  # 替换为目标文件夹路径

# 如果目标文件夹不存在，创建它
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# 遍历源文件夹及其子文件夹中的文件
for dirpath, dirnames, filenames in os.walk(converted):
    for filename in filenames:
        # 检查文件是否是Markdown文件（以 .md 结尾）
        if filename.endswith('.md'):
            # 构建完整的源文件路径和目标文件路径
            source_path = os.path.join(dirpath, filename)
            destination_path = os.path.join(destination_folder, filename)
            
            # 复制Markdown文件到目标文件夹
            shutil.copy(source_path, destination_path)
            print(f"Copied {filename} to {destination_folder}")
