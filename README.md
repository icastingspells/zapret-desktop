﻿# Zapret-desktop


Десктопное приложение для обхода блокировок по DPI 
Основано на проекте zapret by bol-van

[Оригинальный репозиторий](https://github.com/bol-van/zapret)

## Установка

1. zapret.exe запускаем в пустой дериктории
2. Программа автоматически подгрузит все нобходимые файлы с репозитория гитхаб в директорию ```/repo```
3. Программа работает из трея поэтому переходим туда, кликаем пкм по иконке с переключателем и нажимаем "Создать службу"


## Как работает (инструкция по применению)

О процессе обхода блокировок можете прочитать в [Оригинальном репозитории](https://github.com/bol-van/zapret)

- Программа создает службу которая фильтрут наш трафик, ее можно отключать и включать в трее, свитч будет показывать работает ли она
- После первого создания службы больше не нужно ее пересоздавать, все обновления будут выкладываться в гитхаб репозиторий, при появлении новых обновлений вы сможете установить их напрямую из программы, в случае если таковые есть будет доступна кнопка "Установить последнее обновление" 
- Служба запускается автоматически при запуске пк, не нужно каждый раз открывать программу и вручную включать ее
- Отключать службу рекомендуется при появлении проблем с загрузкой различных сервисов, большинство должны работать с включенной программой


## Основные преимущества данной сборки
- Тонкая настройка фильтрации портов, используются только необходимые UDP порты, благодаря чему не ломает работу других программ и не мешают соединению с определенными сервисами
- Устранена проблема с блокировкой технологии ECH которой пользуются хосты CloudFlare
- Упращенное управление работой службы
- Программа будет постоянно обновляться при появлении новых проблем с блокировками 


## За сборку спасибо [HyperBeam](t.me/hyperbeamm)

Welcome to free internet
