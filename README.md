﻿# Zapret-desktop


Десктопное приложение для обхода блокировок по DPI 
Основано на проекте zapret by bol-van

[Оригинальный репозиторий](https://github.com/bol-van/zapret)

## Установка

1. Скачиваем [.exe файл](https://github.com/icastingspells/zapret-desktop/releases/download/executable/zapret.exe)
2. zapret.exe запускаем в пустой дериктории
3. Программа автоматически подгрузит все нобходимые файлы с репозитория гитхаб в директорию ```/repo```
4. Программа работает из трея поэтому переходим туда, кликаем пкм по иконке с переключателем и нажимаем "Создать службу"
5. После перезагрузки ПК, программа становится неактивной, но служба остаётся в рабочем состоянии, для работы переключателя необходимо каждый раз после перезапуска ПК запускать zapret.exe файл (временно)


## Как работает (инструкция по применению)

О процессе обхода блокировок можете прочитать в [Оригинальном репозитории](https://github.com/bol-van/zapret)

- Программа создает службу которая фильтрут наш трафик, ее можно отключать и включать в трее, свитч будет показывать работает ли она
- После первого создания службы больше не нужно ее пересоздавать, все обновления будут выкладываться в гитхаб репозиторий, при появлении новых обновлений вы сможете установить их напрямую из программы, в случае если таковые есть будет доступна кнопка "Установить последнее обновление" 
- Служба запускается автоматически при запуске пк, не нужно каждый раз открывать программу и вручную включать ее
- Отключать службу рекомендуется при появлении проблем с загрузкой различных сервисов, большинство должны работать с включенной программой


## Основные преимущества данной сборки
- Тонкая настройка фильтрации портов, используются только необходимые UDP порты, благодаря чему не ломает работу других программ и не мешают соединению с определенными сервисами
- Устранена проблема с блокировкой технологии ECH которой пользуются хосты CloudFlare
- Упрощенное управление работой службы
- Программа будет постоянно обновляться при появлении новых проблем с блокировками
- Не влияет на пинг, не создает задержки между клиентом и сервером, в играх не будет просадок, не нагружает систему

## Известные проблемы:
- Не работает из автозапуска (возможное решение запуск через планировщих задач с повышенными привелегиями)
- Возможны проблемы на некоторых версиях Windows 10
- Не работает с большинством VPN
- Может ругаться защитник Windows (это нормально т.к. программа не подписанная, потому что ее далели два студента с бутылкой пива)

## За сборку спасибо [HyperBeam](https://t.me/hyperbeamm)

Welcome to free internet
