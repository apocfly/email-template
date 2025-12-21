import os
import shutil
import logging

# 设置日志配置
logging.basicConfig(
    level=logging.INFO,  # 设置日志级别
    format='%(asctime)s - %(levelname)s - %(message)s',  # 设置日志输出格式
    handlers=[
        logging.StreamHandler()  # 输出到控制台
        # 可以添加 FileHandler 让日志写入文件，示例：
        # logging.FileHandler('conversion.log')  
    ]
)

def batch_rename_files(directory, change_to_html=True, output_dir='new'):
    # 获取目录的绝对路径，防止相对路径问题
    abs_directory = os.path.abspath(directory)
    
    # 创建输出目录（如果不存在）
    output_dir = os.path.join(abs_directory, output_dir)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 获取目录下所有的文件
    for filename in os.listdir(abs_directory):
        old_file_path = os.path.join(abs_directory, filename)
        
        # 只处理文件，不处理目录
        if os.path.isfile(old_file_path):
            logging.info(f'Processing file: {old_file_path}')  # 输出当前正在处理的文件路径
            
            # 只处理以 .template 或 .html 结尾的文件
            if filename.endswith('.template') or filename.endswith('.html'):
                if change_to_html:
                    if filename.endswith('.template'):
                        # 正确处理 .template 扩展名（去掉后缀）
                        new_filename = filename[:-9] + '.html'  # 去掉 .template 后缀（8 个字符）
                    else:
                        continue
                else:
                    if filename.endswith('.html'):
                        # 正确处理 .html 扩展名（去掉后缀）
                        new_filename = filename[:-5] + '.template'  # 去掉 .html 后缀（5 个字符）
                    else:
                        continue

                # 输出修改后的文件名和路径
                logging.info(f'Old filename: {filename} -> New filename: {new_filename}')
                
                # 新文件的路径
                new_file_path = os.path.join(output_dir, new_filename)
                
                # 输出重命名的源路径和目标路径
                logging.info(f'Old file path: {old_file_path} -> New file path: {new_file_path}')
                
                # 将文件从源文件夹移动到目标文件夹，并重命名
                shutil.copy(old_file_path, new_file_path)
                logging.info(f'File copied and renamed: {old_file_path} -> {new_file_path}')

# 使用例子:
# 如果你想把 .html 转换回 .template，设置 change_to_html=False
batch_rename_files(r'./new', change_to_html=False, output_dir='new')

# 批量转换 .template 到 .html，并放到 /new/ 文件夹
batch_rename_files(r'.', change_to_html=True, output_dir='new')


