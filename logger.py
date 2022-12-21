# Модуль для записи резуьтатов вычислений

def log_exec(expr: str, result: str):
    """Записывает в файл результат вычислений
    в виде |задача -> ответ|"""
    with open('results.txt', 'a', encoding='utf-8') as f:
        f.write(f'\n Задача: {expr} -> результат: {result} ')


def get_history() -> str:
    """"Возвращает содержимое файла с результатами вычислений"""
    with open('results.txt', 'r', encoding='utf-8') as file:
        line = file.read().split('\n')
        return ('\n'.join(line))

