BOOK_PATH = 'book/Bredberi_Marsianskie-hroniki.txt'
PAGE_SIZE = 1050

book = dict()


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int):
    res = text[start: start + size]
    if len(res) < size:
        return res, len(res)

    if res.endswith("..") or res.endswith("?.") or res.endswith("!."):
        res = res.rstrip("..").rstrip("?.").rstrip("!.")
    is_end = (',', '.', '!', ':', ';', '?')

    while res[-1] not in is_end:
        res = res[:-1]

    return res, len(res)


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path, 'r', encoding='utf-8') as f:
        file = f.read()
    i = 0
    key_dict = 1
    while i < len(file):
        res = _get_part_text(file, i, PAGE_SIZE)
        i += res[1]
        book[key_dict] = res[0].lstrip()
        key_dict += 1


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(BOOK_PATH)
