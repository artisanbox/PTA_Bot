'''
Author：Luo
Date：2020.03.28
Version：1.2.3
Function：Planning Tasks Assistant

'''
from nonebot.command.argfilter import controllers
from nonebot import on_command,CommandSession,command
import os,function.plugins.report
 
  
@on_command('add_group',aliases=('添加群号', 'add_group', '3',), only_to_me=False)
async def add_group(session:CommandSession):  
    your_qq_num = function.plugins.report.your_qq_num()
    number_of_group = function.plugins.report.number_of_group() 
    message_type = session.ctx['message_type']
    user_id = session.ctx['user_id']
    if function.plugins.report.check_default():
        if message_type == 'private' and user_id == int(your_qq_num[0]):
        
            Add_G_N = str(session.get('Add_G_N',prompt='请添加你要管理的QQ群号',
                arg_filters=[controllers.handle_cancellation(session)]))
               
            
            if not Add_G_N.isdigit():
                await session.pause('QQ群号应该是数字,例如：7，8，9')
                
            Add_G_N += ' '    
            
            if function.plugins.report.check_same_group(Add_G_N, number_of_group):
                with open('./function/data/group_number.txt','a') as add_group:
                    add_group.write(Add_G_N)
   
                await session.send('QQ群号添加成功')
            else:
                await session.send('QQ群号重复')
    else:
        await session.send('请先初始化')
        