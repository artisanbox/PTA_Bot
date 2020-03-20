# nonebot_qq
QQ机器人，1、可以定时禁言，2、定时发消息，3、@全体人员
## 使用方法
- 回复机器人：'帮助' 即可获取帮助指令
- 配置自己的QQ号：config/py 中的QQ号修改为自己的即可
- 设置群号：在 function\plugins 中的 report.py 中修改
- 具体问题参看下方
## notbot官方文档：https://nonebot.cqp.moe/
## 安装方法：https://nonebot.cqp.moe/guide/installation.html
## 安装配置:

安装完成后，再次配置CQHTTP插件，打开名为 “user-id”.json 的文件（“user-id” 为你登录的 QQ 账号）
修改文件为如下配置项:
```
{
  "ws_reverse_api_url": "ws://127.0.0.1:8080/ws/api/",
  "ws_reverse_event_url": "ws://127.0.0.1:8080/ws/event/",
  "use_ws_reverse": true
}
```
配置好后重启插件，运行我写的Python文件（bot.py），若配置成功,控制台应该会输出以下内容:

```
[2019-10-01 15:55:21,745] 127.0.0.1:50971 GET /ws/api/ 1.1 101 - 1031
[2019-10-01 15:55:22,044] 127.0.0.1:50972 GET /ws/event/ 1.1 101 - 996
```

这表示 CQHTTP 插件已经成功地连接上了 NoneBot，与此同时，插件的日志文件中也会输出反向 WebSocket 连接成功的日志。

