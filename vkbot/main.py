from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime
import random


token = "65b24cf377ed135152d40cae1b8f07873853960d1ba32084c111ebc309ea9261fb1fd8d7b9ba1153d46f1"
vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), '%H:%M:%S')))
            print('Текст сообщения: ' + str(event.text))
            print(event.user_id)
            response = event.text.lower()
            if event.from_user and not (event.from_me):
                if response == 'привет':
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Привет', 'random_id': 0})