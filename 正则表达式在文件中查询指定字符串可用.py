# -*- coding: utf-8 -*-
#基础参数部分
base_dir='C:\\Users\\\zhang\\Desktop\\backup\\logs\\'#基础目录
IP='167'#目录下面的IP子文件夹
file_name='\\send_report_via_tarlog_20151231.log'#最终的日志文件
file_name_full_path=base_dir+IP+file_name
text=['邮件发送成功','备份文件为','当前备份的文件大小是','正在发送至']#定义要查找的多个字符串
#查找函数
def find_message(files,server_ip):#查找文件里面的内容
    file_context = open(files)#打开文件进行读取
    for line in file_context:#定义line变量读取文件每一行内容
        for text_str in text:#定义待查询的字符串每一个元素
            if not line.find(text_str)== -1:
                print "%s服务器\n%s"%(server_ip,line) #打印当前行，并显示是哪个服务器的日志
    file_context.close() #关闭文件
find_message(file_name_full_path,IP)
