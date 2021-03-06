import os,sys
kindlegen_path = r"lib\kindlegen.exe"
kindlestrip_path = r"lib\kindlestrip.exe"
if not os.path.exists(kindlegen_path):
    print("kindlegen.exe 不存在！")
    input()
    os._exit()
if not os.path.exists(kindlestrip_path):
    print("kindlestrip.exe 不存在！")
    input()
    os._exit()

print("My kindle tools: Epub To Kindle Mobi")
print("Created by Ueino Hakono")
print("v1.0")
print()
if len(sys.argv) <2:
    print("请传入要转换的书籍目录！")
    input()
    os._exit(0)

print("待转换的文件：")
epubs = sys.argv[1:]

for epub_path in epubs:
    print(epub_path)
print()
print("**************开始转换**************")
for idx,epub_path in enumerate(epubs):
    print("%d. 开始转换: %s" % (idx+1,epub_path))
    if not os.path.exists(epub_path):
        print("此文件不存在")
        continue
    status =  os.system('%s "%s"' % (kindlegen_path,epub_path))

    epub_file_name = os.path.basename(epub_path)
    epub_dir_path = os.path.dirname(epub_path)
    mobi_file_name = os.path.splitext(epub_path)[0] + ".mobi"
    mobi_file_path = os.path.join(epub_dir_path,mobi_file_name)

    if not os.path.exists(mobi_file_name):
        print()
        print("!!!!!!!!!!!!!!!!!转换失败!!!!!!!!!!!!!!!!!!")
        print("  epub转换失败: %s"% (mobi_file_path))
        print("  如果上方的失败原因为： 错误(xmlmake):E27012: 已经使用项或进程标识符 \n    则原因在epub文件有问题。请用Calibre将此epub转为epub来使其格式正确！")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("输入回车开始转换下一本")
        input()

        continue
    print("epub转换完成，新mobi文件：%s" % mobi_file_path)
    print("开始为epub瘦身...")
    before_size = os.path.getsize(mobi_file_path)/1024/1024
    status = os.system('%s "%s" "%s"' % (kindlestrip_path,mobi_file_path,mobi_file_path))
    after_size = os.path.getsize(mobi_file_path)/1024/1024
    print("瘦身完成：%.1fMB -> %.1fMB" %(before_size,after_size))
    print("转换完成")
    print()