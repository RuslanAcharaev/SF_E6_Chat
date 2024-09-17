<h2 align="center">Онлайн чат</h2>

Онлайн чат написан с использованием фреймворка <a href="https://www.djangoproject.com/" target="_blank">Django</a> и библиотеки <a href="https://channels.readthedocs.io/en/latest/" target="_blank">django-channels</a>.

Также при создании были использованы такие пакеты, как:
<a href="https://docs.allauth.org/en/latest/" target="_blank">django-allauth</a> для регистрации и аутентификации и <a href="https://www.django-rest-framework.org/" target="_blank">Django REST framework</a> для создания API. Для оформления сайта был использован фреймворк <a href="https://tailwindcss.com/" target="_blank">TailwindCSS</a>.

Полный список необходимых для установки пакетов собран в файле *req.txt*.

Запуск сервера производится командой `python manage.py runserver`. Убедитесь, что у Вас запущен **ASGI/Daphne** сервер. Также для корректной работы приложения требуется запущенный сервер **Redis** с портом 6379.

Чтобы проверить коммуникацию с Redis, запустите командную строку Django и введите следующий код:
```python
python manage.py shell
>>>import channels.layers
>>>channel_layer = channels.layers.get_channel_layer()
>>>from asgiref.sync import async_to_sync
>>>async_to_sync(channel_layer.send)('test_channel', {'type': 'hello'})
>>>async_to_sync(channel_layer.receive)('test_channel')
{'type': 'hello'}
```
----
Главная страница сайта доступна по адресу http://127.0.0.1:8000/
Для того, чтобы использовать чат нужно пройти регистрацию. Профиль пользователя (отображаемое имя, аватар) можно отредактировать, используя пункт *"Редактировать"*  в выпадающем списке по имени пользователя в навигационном меню. Также в навигационном меню имеются ссылки*"Пользователи"*и*"Общий чат"*.
*"Общий чат"*ведет на главную страницу сайта, которая представлена формой для создания новой комнаты и список уже существующих. Ссылка*"Пользователи"*  ведет на страницу http://127.0.0.1:8000/profiles/ , на которой выводится список всех пользователей и можно начать личную переписку с конкретным пользователем.
Общение, установка websocket соединения, отправка и прием сообщений осуществляется по адресу `http://127.0.0.1:8000/chat/room/<int:pk>/`. Комнаты с личной перепиской имеют аттрибут `is_private` со значением `True`. При попытке зайти в комнату с чужой личной перепиской пользователю будет выведена страница с ошибкой 404.
API доступно по адресу http://127.0.0.1:8000/api/

