# Factorial Calculator Module

## Описание

Factorial Calculator Module — это простая и эффективная библиотека на языке Python, предоставляющая функции для вычисления факториала числа. Модуль поддерживает как итеративный, так и рекурсивный методы вычисления факториала, обеспечивая оптимальную производительность и удобство использования.

## Требования

- Python 3.6 и выше

## Установка

Клонируйте репозиторий и импортируйте модуль в ваш проект:

```bash
git clone https://github.com/username/factorial-calculator.git
cd factorial-calculator
```

После клонирования репозитория вы можете импортировать функции в свой код:

```python
from factorial import factorial_iterative, factorial_recursive
```

## Использование

Модуль предоставляет два метода вычисления факториала:

### Итеративный метод

```python
from factorial import factorial_iterative

number = 5
result = factorial_iterative(number)
print(f"Факториал числа {number} равен {result}")  # Вывод: Факториал числа 5 равен 120
```

### Рекурсивный метод

```python
from factorial import factorial_recursive

number = 6
result = factorial_recursive(number)
print(f"Факториал числа {number} равен {result}")  # Вывод: Факториал числа 6 равен 720
```

## Примеры кода

### Итеративная реализация

```python
def factorial_iterative(n):
    """
    Вычисляет факториал числа итеративным методом.
    
    Args:
        n (int): Неотрицательное целое число
        
    Returns:
        int: Факториал числа n
        
    Raises:
        ValueError: Если n отрицательное
    """
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    if n == 0 or n == 1:
        return 1
        
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```

### Рекурсивная реализация

```python
def factorial_recursive(n):
    """
    Вычисляет факториал числа рекурсивным методом.
    
    Args:
        n (int): Неотрицательное целое число
        
    Returns:
        int: Факториал числа n
        
    Raises:
        ValueError: Если n отрицательное
    """
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)
```

## Обработка ошибок

Модуль включает проверку входных данных и обработку следующих ошибок:

- Отрицательные числа вызывают ValueError
- Для слишком больших чисел может возникнуть RecursionError (в рекурсивной реализации) или OverflowError

Пример обработки ошибок:

```python
try:
    result = factorial_iterative(-5)
except ValueError as e:
    print(f"Ошибка: {e}")  # Вывод: Ошибка: Факториал отрицательного числа не определен
```

## Производительность

- Итеративный метод более эффективен по памяти и рекомендуется для больших чисел
- Рекурсивный метод более прост для понимания, но имеет ограничения по глубине рекурсии

## Автор

- Сапрыкин Вадим — разработчик

## Лицензия

Этот проект лицензирован под MIT License — подробности см. в файле [LICENSE](LICENSE)
