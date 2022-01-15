# mystbackuper
Backup keystore folder from linux-based Mysterium nodes

Скрипт для бэкапа Mysterium нод, работающих на линукс серверах. Протестировано на ubuntu-20.04.
Скрипт копирует содержимое папки keystore на локальный компьютер. 
Подробнее про процесс миграции ноды в [документации](https://docs.mysterium.network/node-runners/node-migration/).

# Настройка и запуск:
1. Установить Python (протестировано на 3.8) с [официального сайта](https://www.python.org/downloads/). При установке обязательно добавить python в PATH.
2. Скачать данный репозиторий через git или архив (Code -> Download ZIP).
3. Открыть репозиторий в терминале и выполнить команду `python -m pip install -r requirements.txt`.
4. В тестовом редакторе открыть `config.yaml` и указать данные для подключения к серверам согласно шаблону.
5. В терминале выполнить команду  `python backup.py`. 
6. В корне репозитория будут созданы папки с названием сервера. Внутри содержатся файлы для восстановления ноды.

## Протестированные VPS для запуска нод:
* [cp.zomro.com](https://zomro.com/?from=296803)
* [vultr.com](https://www.vultr.com/?ref=8883507)
* [macloud.ru](https://macloud.ru/?partner=qby7f922cx) - по ссылке вечная скидка 10%
* [firstbyte.ru](https://firstbyte.ru/?from=97279)

###Donate:
* MATIC/MYST: 0x37eD168ad499E9F1C7A44b6BCd4d7aef28BD6501
