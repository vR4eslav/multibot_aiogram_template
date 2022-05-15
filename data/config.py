from pathlib import Path

from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = list(map(int, env.list("admins")))  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста

DB_USER = env.str('DB_USER')  # имя владельца бд
DB_PASS = env.str('DB_PASS')  # пароль владельца
DB_NAME = env.str('DB_NAME')  # имя базы данных
DB_HOST = env.str('DB_HOST')  # ip базы (если на одном сервере, то в .env localhost

I18N_DOMAIN = "mybot"
BASE_DIR = Path(__file__).parent
LOCALES_DIR = "locales"  # тут хранятся переводы

POSTGRES_URI = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"

account_payment = env.int("account_payment")

MAIN_BOT_USERNAME = "megatestbot_bot_bot"
