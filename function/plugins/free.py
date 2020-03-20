'''
Author：Luo
Date：2020.03.20
Version：1.1.5
Function：Ban group and send some messages

'''

from nonebot import on_command,CommandSession
from datetime import datetime
import nonebot,time,function.plugins.report


number_of_group = function.plugins.report.number_of_group() #修改你要控制的群号
notice_of_free = function.plugins.report.notice_of_free() #修改你每天早上要通知的内容


@on_command('free', aliases=('定时解除', 'free', '1',), only_to_me=False)
async def free(session: CommandSession):
    global number_of_group,notice_of_free
    message_type = session.ctx['message_type']
    duration = str(session.get('duration', prompt='明天几点钟解除禁言呀？'))
    if not duration.isdigit():
        await session.pause('时间应该是数字,例如：7，8，9')
    notice_of_free += str(session.get('notice_of_free', prompt='解除禁言后你想通知什么内容？'))
    at_notice = str(session.get('at_notice', prompt='你想@全员吗？'))
    if at_notice.find('不') != -1:
        notice_of_free += '[CQ:at,qq=all]'
    await session.send('定时解除设置成功')
    while True:
        if int(time.strftime("%H", time.localtime())) == int(duration) and message_type == 'private': 
            await session.bot.set_group_whole_ban(group_id = number_of_group,enable = False)
            await session.bot.send_group_msg(group_id = number_of_group,message = notice_of_free)  
            break
            
 
@free.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg and stripped_arg.isdigit():
            session.state['duration'] = int(stripped_arg)
        return

    if not stripped_arg:
        session.pause('时间不能为空呢，请重新输入')

    if stripped_arg.isdigit():
        session.state[session.current_key] = int(stripped_arg)
    
  
  
          
