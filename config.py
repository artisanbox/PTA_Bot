'''
Author：Luo
Date：2020.03.28
Version：1.2.3
Function：Planning Tasks Assistant

'''
from nonebot.default_config import *

SUPERUSERS = {123456}
NICKNAME = {'小明','小猪'}
COMMAND_START = {'', '/', '!', '／', '！'}
SESSION_CANCEL_EXPRESSION = (
    '当前对话已终止',
)
MAX_VALIDATION_FAILURES = 5
TOO_MANY_VALIDATION_FAILURES_EXPRESSION = (
    '你输错太多次啦，需要的时候再叫我吧',
)