

channels = []

def websocket_receive(message):
    text = message.content.get('text')

    if text =='CONNECTED':
        channels.append(message.reply_channel)
    elif text:
        for channel in channels:
            channel.send({"text": "{}".format(text)})


def websocket_connect(message):
    print('websocket --->CONNECTED')
