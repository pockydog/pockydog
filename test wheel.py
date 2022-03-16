# # git
# # **
# # class
# # file
# # import re
# # a = https://steam.oxxostudio.tw/category/python/basic/inheritance.html
# print(a)
# # https://hackmd.io/1XuDG3lJTZGuLL4Zao8fmg\
# a = https://yuhsiangfu.gitbooks.io/ice101-basic-python-programming-and-data-analysis/content/class-6-han-shu/64-can-zhao-ji-chuan-ru-can-zhao.html
# https://www.delftstack.com/zh-tw/howto/python/python-change-dictionary-value/
# https://www.delftstack.com/zh-tw/tutorial/python-modules-tutorial/python-regular-expression/#%E4%BD%BF%E7%94%A8-sub-%E5%87%BD%E5%BC%8F%E4%BE%86%E5%88%AA%E9%99%A4%E5%AD%97%E4%B8%B2%E4%B8%AD%E7%9A%84%E6%89%80%E6%9C%89%E6%95%B8%E5%AD%97
# https://www.jb51.net/shouce/jquery/regexp.html
# https://www.learncodewithmike.com/2020/01/python-module-and-package.html


'''

https://steam.oxxostudio.tw/category/python/basic/builtin-eval-exec.html

Try:
http://kaiching.org/pydoing/py/python-raise.html

https://www.memeta.co/zh-Hant/article/1eaqk_1fwpu.html

https://blog.csdn.net/weixin_43347550/article/details/105291462?spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1.pc_relevant_default&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1.pc_relevant_default&utm_relevant_index=2

- 建制專案
    step 1. git clone <網址>
    step 2. cd ~/project_name
    step 3. git checkout develop
    step 4. git submodule
    step 5. git submodule init
    step 6. git submodule update
    step 7. cd src/XXX_common
    step 8. git checkout develop


＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿

- XXX_service:是用來建置專案的相關服務（mysql、phpmyadmin、redis）

名稱有帶service的專案，通常都是在起 其他相關服務 例如資料庫 快取資料庫

＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿

那么，__init__()和__call__()的区别如下：
1. __init__()的作用是初始化某个类的一个实例。
2. __call__()的作用是使实例能够像函数一样被调用，同时不影响实例本身的生命周期（__call__()不影响一个实例的构造和析构）。但是__call__()可以用来改变实例的内部成员的值。

https://blog.csdn.net/yjk13703623757/article/details/77918633


＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
Exec = 執行
wrapper 包裝

＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿
裝飾器：
https://ithelp.ithome.com.tw/articles/10200763
https://dev.to/codemee/python-decorator-3bni

'''

'''
<src> 支援的作業系統和可以開啟該檔案類型的相關軟體或應用程式
-<core>核心/放重要
通常會有__init__初始化，一堆handler（相關API主要邏輯實作的地方）
-<general>別的也需要用這些工具的專案
-<commom>執行的
-<script>放腳本的地方/存放專案的一些可執行檔案
-<utils>中文為’配置’，也是放置工具的地方，一般來說，常常用來描述和業務邏輯沒有關係的資料處理。 Util一般要和私有方法對比：私有方法一般來說是隻是在特地場景下使用的
配置
- 入口點是在程式中執行第一條指令的地方，和程式存取命令列參數的地方。通常會取名為main.py，公司為start.......start_XXXXXX 就是所有專案的啟動檔


.dockerignore   = 可以填入所有不提供給git push的東西
.gitgnore  = 可以填入所有不提供給git push的東西
.gitmodules
dev.env
Docker-compose.yml =  有助於定義和共用多容器應用程式。 使用 
Docker Compose，您可以建立檔案來定義服務。 您可以使用單一命令來啟動所有專案，或將其全部拉低。
您可以在檔案中定義您的應用程式堆疊，並在版本控制下將該檔案保存在專案存放庫的根目錄。 這種方法可讓其他人參與您的專案。 它們只需要複製您的存放庫。是用於定義和運行多個容器的Docker生態系相關工具。


Dockerfile = 簡單的文字檔，其中包含使用者可以呼叫組裝映像檔的指令，
README.md = 軟體定位，軟體的基本功能
Requirements.txt  = 用於記錄所有依賴包及其精確的版本號。存放軟體依賴的外部Python包列表

'''

#
# class Example:
#     def __init__(self):
#         print("Instance Created")
#
#     def __call__(self):
#         print("Instance is called via special method")
#
#
# e = Example()
# e()

# def out(func):
#     def inter(a):
#         return func(a)
#     return inter
#
# def check_str(func):
#     def inner():
#         print('woow')
#         return func()
#     return inner()

# @check_str
# def show():
#     print('toot')

def printHello(func):
    def wrapper():
        print('Hello')
        return func()
    return wrapper

@printHello
def printWorld():
    print('World')

# printWorld()

import time


def timing(func):
    def wrapper():
        print("Start...")
        t1 = time.perf_counter()
        func()
        t2 = time.perf_counter()
        print(t2)
        print(t1)
        print(t2 - t1)
    return wrapper

@timing
def works():
    total = 0
    for i in range(10000):
        total += i
    print(total)
works()
