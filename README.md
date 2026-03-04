# Rusimkabot

### Branches
- `userbot`: ветка для создания телеграмм бота для пользователей 
- `adminbot`: ветка для создания телеграмм бота для администраторов
- `main`: основная ветка где будут релизные версии бота

### Структура файловой системы
- `main.py`: файл запуска созданных ботов
- `bot/`: функции для создания телеграмм ботов, администратора
- `handler/`: обработчики событий
- `filters/`: фильтры сообщений
- `database/`: базы данных ORM

### Инициализация проекта:

#### Получение репозитория:
```shell
git clone "https://github.com/Cyberamirka/Rusimkabot.git"
```

#### Инициализация в папке проекта окружения
```shell
cd Rusimkabot
python -m venv .venv/
```

#### Активация окружения:

##### Windows:
```shell
.venv\Scripts\activate.bat
```

##### *nix
```shell
soruce .venv/bin/activate
```

### Установка всех зависимостей

После активации окружения python, можно установить необходимые зависимости
```shell
pip install --upgrade pip
pip install -r requirements.txt
```

### Используемый стек технологий:
- python 3.14
- aiogram
- dotenv
- logging
- postgresql
- sqlalchemy
- redis