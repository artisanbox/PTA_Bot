'''
Author：Luo
Date：2020.03.21
Version：1.2.0
Function：Banned timing and send some messages

'''

import datetime,time,function.plugins.report
from apscheduler.triggers.date import DateTrigger # 一次性触发器
# from apscheduler.triggers.cron import CronTrigger # 定期触发器
# from apscheduler.triggers.interval import IntervalTrigger # 间隔触发器
from nonebot import on_command, scheduler, CommandSession


number_of_group = function.plugins.report.number_of_group() #在config.py中修改群号
notice_of_free = function.plugins.report.notice_of_free() 


@on_command('free_group', aliases=('定时解除', 'free_group', '1',), only_to_me=False)
async def free_group(session: CommandSession):
    global number_of_group,notice_of_free
    message_type = session.ctx['message_type']
    user_id = session.ctx['user_id']
    if message_type == 'private' and user_id == function.plugins.report.your_qq_num():
        duration = str(session.get('duration', prompt='明天几点钟解除禁言呀？例如7-45'))
        duration = duration.split('-')
        if not duration[0].isdigit() and not duration[1].isdigit():
            await session.pause('时间应该是数字,例如：7，8，9')
        notice_of_free = session.get('notice_of_free', prompt='解除禁言后你想通知什么内容？')
        at_notice = str(session.get('at_notice', prompt='你想@全员吗？'))
        if at_notice.find('不') == -1:
            notice_of_free += '[CQ:at,qq=all]' 
        await session.send('定时解除设置成功')
        duration_hours = int(duration[0]) - int(time.strftime("%H", time.localtime()))
        duration_mins = int(duration[1]) - int(time.strftime("%M", time.localtime()))
        
        #触发器
        delta = datetime.timedelta(minutes = (duration_mins + duration_hours * 60))
        trigger = DateTrigger(
            run_date = datetime.datetime.now() + delta
        )
        
        #添加任务
        scheduler.add_job(
            func=session.bot.send_group_msg,  # 要添加任务的函数，不要带参数
            trigger=trigger,  # 触发器
            #args=(12345,),  # 函数的参数列表，注意：只有一个值时，不能省略末尾的逗号
            kwargs={'group_id':number_of_group,'message' :notice_of_free}
            #misfire_grace_time=60,  # 允许的误差时间，建议不要省略
            #jobstore='default',  # 任务储存库，在下一小节中说明
        )
            
        scheduler.add_job(
            func=session.bot.set_group_whole_ban,  
            trigger=trigger,  
            kwargs={'group_id':number_of_group,'enable' : False}
        )
    
@free_group.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg and stripped_arg.isdigit():
            session.state['duration'] = int(stripped_arg)
        return

    if not stripped_arg:
        session.pause('时间不能为空呢，请重新输入')   
    