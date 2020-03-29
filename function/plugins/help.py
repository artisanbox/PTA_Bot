'''
Author：Luo
Date：2020.03.28
Version：1.2.3
Function：Planning Tasks Assistant

'''

from nonebot import on_command,CommandSession
import nonebot


@on_command('help', aliases=('帮助',))
async def help(session: CommandSession):
    message_type=session.ctx['message_type']
    if message_type == 'private':
        await session.send('''0.初始化数据<初始化>
1.定时解除群禁言<定时解除>
2.定时开始群禁言<定时禁言>
3.添加你要的控制QQ群<添加群号>
4.中断当前对话<取消>
(未初始化请先初始化)''')


