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
