from dataclasses import dataclass
from environs import Env
from typing import List


@dataclass
class TgBot:
    token: str
    admin_ids: List[int]


@dataclass
class Config:
    tg_bot: TgBot


# Создаем функцию, которая будет читать файл .env и
# возвращать экземпляр класса Config с заполненными полями token и admin_ids
def load_config(path: str) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN'),
                               admin_ids=list(map(int, env.list('ADMIN_IDS')))))

# print(load_config('.env'))
