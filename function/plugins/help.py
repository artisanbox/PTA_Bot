'''
Author：Luo
Date：2020.03.19
Version：1.1.0
Function：Ban group and send some messages

'''

from nonebot import on_command,CommandSession
import nonebot


@on_command('help', aliases=('帮助',))
async def help(session: CommandSession):
    message_type=session.ctx['message_type']
    if message_type == 'private':
        await session.send('''1.定时解除禁言
2.立即禁言
给机器人发送对应数字即可''')


