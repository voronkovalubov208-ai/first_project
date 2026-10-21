import os
from dotenv import load_dotenv

def print_author():
    # 1. Загружаем переменные из файла .env в память
    load_dotenv() 
    
    # 2. Читаем значение переменной AUTHOR
    author = os.getenv("AUTHOR") 
    
    # 3. Печатаем результат
    print(f"Автор проекта: {author}")

# Вызов функции, чтобы проверить её работу
if __name__ == "__main__":
    print_author()