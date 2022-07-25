# -*- coding:utf-8 -*-
目的：当有人用你的电脑时，会调用此软件（需要自己创建启动项）进行开启摄像头进行拍照，然后发送给自己的邮箱。
注：需要自己百度(给个添加启动项的链接https://zhuanlan.zhihu.com/p/265076894)。

1.首先需要安装opencv-python库和smtplib库。

2.需要改动zh_pwd.ini文件里面的账号和授权码。

3.运行程序，有错找错，没错就大功告成。

注：

    1.建议通过pyinstaller库打包成exe文件，然后生成快捷方式进行开机启动。

    2.打包命令：（打开cmd，切换到程序路径，使用命令打包，打包的exe文件在dist文件夹里，需要将zh_pwd.ini文件复制到这个文件夹一份）
    
        简单版：pyinstaller -w -F python程序名.py
        
        复杂版：pyinstaller -w -i 图标名.ico -F python程序名.py   #图标需要和程序在同一个文件夹
