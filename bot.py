'''
Author：Luo
Date：2020.03.28
Version：1.2.3
Function：Planning Tasks Assistant

'''
import nonebot
import config
from os import path

if __name__ == "__main__":
	nonebot.init(config)
	nonebot.load_plugins(
		path.join(path.dirname(__file__),"function","plugins"),
		"function.plugins"
		)
	nonebot.run(host='127.0.0.1', port=8080)
