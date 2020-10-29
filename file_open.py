"""
    file_open.py
    文件打开方式示例
    总结：任何文件都可以用二进制方式打开
         二进制文件不会使用文本方式打开
"""

# 打开文件
# f = open('../day01/hello.py', 'r') # 只读
# f = open('file.txt', 'w') # 只写
# f = open('file.txt', 'a') # 追加写
f = open('file.txt', 'rb')  # 二进制方式打开
print(f)
# 读写文件

# 关闭文件
f.close()