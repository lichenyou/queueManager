

import login
import pymysql
import threading
import time
import socket
import json
#读取数据库
#批量上号
import Queue
#获取账号状态

# coding: utf-8
# 定义具体的任务进程，具体的工作任务是什么

import time, sys, queue
from multiprocessing.managers import BaseManager
import maxThread

# 创建类似的QueueManager,继承BaseManager,用于后面创建管理器

class QueueManager(BaseManager):
    pass

# 第一步：使用QueueManager注册用于获取Queue的方法名称
# 前面服务进程已经将队列名称暴露到网络中，
# 该任务进程注册时只需要提供名称即可，与服务进程中队列名称一致
if __name__ == '__main__':

    QueueManager.register('get_task_queue')
    QueueManager.register('get_result_queue')

    # 第二步：连接到服务器,也就是运行服务进程代码的机器
    server_addr = '127.0.0.1'
    print("Connet to server %s..." % server_addr)
    # 创建一个管理器实例，端口和验证口令保持与服务进程中完全一致
    m = QueueManager(address=(server_addr, 8001), authkey=b'abc')
    # 连接到网络服务器
    m.connect()

    # 第三步：从网络上获取Queue对象，并进行本地化，与服务进程是同一个队列
    task = m.get_task_queue()
    result = m.get_result_queue()

    # 第四步：从task队列获取任务，并把结果写入到resul队列
    for i in range(10):
        try:
            # 前面服务进程向task队列中放入了n,这里取出n
            # n和n相乘，并将相乘的算式和结果放入到result队列中去
            n = task.get(timeout=1) # 每次等待1秒后取出任务
            print("run task %d * %d..." % (n, n))
            r = '%d * %d = %d' % (n, n, n*n)
            time.sleep(1)
            maxThread.testMaxThread()
            result.put(r)
        except queue.Empty:
            print("task queue is empty.")

    # 任务处理结束
    print("worker exit.")


def implement():
    global count
    loginMacCode = "77f3b9db9e37dc54622ae068af70de27f9b20ab4"
    password = "111111"
    username = "18726390359"
    user1 = login.userLogin(username, password, loginMacCode)
    user1.Login()      #登陆必须使用多线程，每个线程内存在逻辑休眠



    loginMacCode = "6917084f347c9e50963a675e099e249a"
    password = "111111"
    username = "18297939624"
    user2 = login.userLogin(username, password, loginMacCode)
    user2.Login()
    return True


#数据库练习

# from pymysql import *
# def main():
#     # 创建Connection连接
#     conn = connect(host='localhost',port=3306,user='root',password='lcy159357',database='test_db',charset='utf8')
#     # 获得Cursor对象
#     cs1 = conn.cursor()
#     # 执行select语句，并返回受影响的行数：查询一条数据
#     count = cs1.execute('select * from fatboy_hobby;')
#     # 打印受影响的行数
#     print("查询到%d条数据:" % count)
#
#     for i in range(count):
#         # 获取查询的结果
#         result = cs1.fetchone()
#         # 打印查询的结果
#         print(result)
#         # 获取查询的结果
#
#     # 关闭Cursor对象
#     cs1.close()
#     conn.close()
#