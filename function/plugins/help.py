'''
Author：Luo
Date：2020.03.21
Version：1.2.0
Function：Banned timing and send some messages

'''

from nonebot import on_command,CommandSession
import nonebot


@on_command('help', aliases=('帮助',))
async def help(session: CommandSession):
    message_type=session.ctx['message_type']
    if message_type == 'private':
        await session.send('''1.定时解除禁言
2.定时禁言
给机器人发送对应数字即可''')


