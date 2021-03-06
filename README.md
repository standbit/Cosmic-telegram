# Космический Telegram 
Консольная утилита. Достает красивые картинки и фото космических объектов из API NASA и SpaceX. Постит их в телеграм-канал посредством бота с настраиваемой периодичностью.

## Установка программы
Python3 должен быть установлен
1. Склонируйте репозиторий к себе на компьютер

2. Дальше работайте в консоли. Cоздайте папку виртуального окружения
```python
$ virtualenv venv
```
3. Активируйте виртуальное окружение для изоляции проекта
```python
$ source venv/bin/activate
```
4. Установите зависимости, используя `pip`
```python
$ python3 -m pip install -r requirements.txt
```
5. Сгенерируйте токен для авторизации на сайте [NASA](https://api.nasa.gov/)

## Переменные окружения
В программе используются четыре переменные окружения:
- `NASA_TOKEN` - это токен, который получаете на сайте NASA
- `TG_TOKEN` - это токен телеграм-бота
- `TG_CHAT_ID` - это ссылка на канал, где будут поститься фото
- `SLEEP_TIME` - время, устанавливающее периодичность публикации фото в канале (по умолчанию 1 сутки)

## Запуск скрипта
1. Запустите скрипт, загружающий фото запусков SpaceX:
```python
$ python3 fetch_spacex.py
```
2. Запустите скрипт, загружающий фото NASA:
```python
$ python3 fetch_nasa.py
```
3. Запустите скрипт, публикующий фото в телеграм-канал:
```python
$ python3 main.py
```
4. Остановить выполнение программы в консоли: `Ctrl+C`

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](http://dvmn.org/)
