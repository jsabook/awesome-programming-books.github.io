path = "." #文件夹目录
template = """# Preface

📚经典技术书籍 PDF 文件，涵盖：编程语言、计算机系统、网络协议、数据库、代码艺术、设计模式、算法与数据结构、系统架构、微服务、测试、程序员职业修炼等相关书籍。

> 如有侵权，请联系删除！


"""
def list_all_files(rootdir):
    import os
    _files = []

    # 列出文件夹下所有的目录与文件
    list_file = os.listdir(rootdir)

    for i in range(0, len(list_file)):

        # 构造路径
        path = os.path.join(rootdir, list_file[i])

        # 判断路径是否是一个文件目录或者文件
        # 如果是文件目录，继续递归
        if "." ==list_file[i][0]:
            continue
        if os.path.isdir(path):
            _files.extend(list_all_files(path))
        if os.path.isfile(path):
            _files.append([rootdir,path])
    return _files

files = list_all_files(path)
# files = [file.replace("\\", "/") for file in files]
import pandas as pd 
pd_files = pd.DataFrame(files)
for dir_name, group in pd_files.groupby(0):
    if dir_name ==path:
        continue
    dir_name = dir_name.replace(path,"").replace('\\','')
    part_template = "## "+dir_name
    for row in group.iterrows():
        file_path = row[1][1].replace('\\','/')
        file_name = file_path.split('/')[-1]
        part_template =part_template + "\n- [%s](%s)"%(file_name,file_path)
    template = template +'\n'+part_template
print(template)

with open("README.md",'w+',encoding='utf-8') as f:
    f.write(template)