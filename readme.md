logger.py - генератор логов
запуск генератора: python3 logger.py

counter.awk - подсчет количества запросов на сервер
запуск: awk -f counter.awk <file name> (в данном случае log.txt)

errors.awk - вывод всех строк с ошибками
запуск: awk -f counter.awk <file name> (в данном случае log.txt)

longest.sh - вывод топ 10 самых долгих команд
запуск: ./longest.sh (возможно сперва надо дать скрипту права на исполнение chmod 777 longest.sh)

top_users.sh - вывод топ 10 пользователей, от которых было больше всего запросов
запуск ./top_users.sh
