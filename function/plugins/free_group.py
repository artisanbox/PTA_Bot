'''
Author：Luo
Date：2020.03.28
Version：1.2.3
Function：Planning Tasks Assistant

'''

import datetime,time,function.plugins.report
from apscheduler.triggers.date import DateTrigger 
from nonebot import on_command, scheduler, CommandSession
from nonebot.command.argfilter import controllers





@on_command('free_group', aliases=('定时解除', 'free_group', '1',), only_to_me=False)
async def free_group(session: CommandSession):
    number_of_group = function.plugins.report.number_of_group() 
    your_qq_num = function.plugins.report.your_qq_num()
    message_type = session.ctx['message_type']
    user_id = session.ctx['user_id']
    if function.plugins.report.check_default():
        if message_type == 'private' and user_id == int(your_qq_num[0]):
            
            duration = str(session.get('duration', prompt='什么时候解除禁言呀？例如7-45',
                arg_filters=[controllers.handle_cancellation(session)]))
                
            duration = duration.split('-')
            
            if not duration[0].isdigit() and not duration[1].isdigit():
                await session.pause('时间应该是数字,例如：7，8，9')
                
            notice_of_free = session.get('notice_of_free', prompt='解除禁言后你想通知什么内容？',
                arg_filters=[controllers.handle_cancellation(session)])
            
            notice_of_free += '[CQ:at,qq=all]' 
            await session.send('定时解除设置成功')
            
            duration_hours = int(duration[0]) - int(time.strftime("%H", time.localtime()))
            duration_mins = int(duration[1]) - int(time.strftime("%M", time.localtime()))
            
            #触发器
            delta = datetime.timedelta(minutes = (duration_mins + duration_hours * 60))
            trigger = DateTrigger(
                run_date = datetime.datetime.now() + delta
            )
            
            for i in range(len(number_of_group)):
                #添加任务
                scheduler.add_job(
                    func=session.bot.send_group_msg,
                    trigger=trigger,  
                    kwargs={'group_id':int(number_of_group[i]),'message' :notice_of_free},
                    misfire_grace_time=60,   
                )
                    
                scheduler.add_job(
                    func=session.bot.set_group_whole_ban,  
                    trigger=trigger,  
                    kwargs={'group_id':int(number_of_group[i]),'enable' : False} 
                )
    else:
        await session.send('请先初始化')
          