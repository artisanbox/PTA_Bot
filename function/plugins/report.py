'''
Author：Luo
Date：2020.03.28
Version：1.2.3
Function：Planning Tasks Assistant

'''
from nonebot.command.argfilter import controllers
from nonebot import on_command,CommandSession
import os
         
 
def check_same_group(Add_G_N, group_qq_num):
    check_times = 0
    for i in range(len(group_qq_num)-1):
        if Add_G_N == group_qq_num[i]:
            check_times+=1
    if check_times==0:
        return True

def check_default():
    if not os.path.getsize('./function/data/self_number.txt') or\
        not os.path.getsize('./function/data/group_number.txt'):   
        return False
    else:
        return True
        
def number_of_group(): 
    with open('./function/data/group_number.txt','r') as group: 
        number_of_group = group.readlines()[0].split()
        return number_of_group

def your_qq_num():
    with open('./function/data/self_number.txt','r') as self: 
        your_qq_num = self.readlines()
        return your_qq_num


@on_command('default',aliases=('初始化', 'default', '0',), only_to_me=False)
async def default(session:CommandSession):
    message_type = session.ctx['message_type']
    if message_type == 'private': 
        if not os.path.getsize('./function/data/self_number.txt')\
            or not os.path.getsize('./function/data/group_number.txt'):
            
            G_N = str(session.get('G_N',prompt='请初始化你要管理的一个QQ群号',
                arg_filters=[controllers.handle_cancellation(session)]))
            G_N += ' ' 
            
            S_N = str(session.get('S_N',prompt='请输入你自己的QQ号',
                arg_filters=[controllers.handle_cancellation(session)]))  
                
            with open('./function/data/group_number.txt','a') as all_group:
                all_group.write(G_N)  
            
            with open('./function/data/self_number.txt','a') as self_qq:
                self_qq.write(S_N)
                
            await session.send('初始化设置成功') 
            
        else:
            await session.send('不可以重复初始化') 
  
        