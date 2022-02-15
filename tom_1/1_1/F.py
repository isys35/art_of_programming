
def euclidean_algorithm(m: int, n: int) -> int:
    """
    Алгоритм Евклида.
    Позволяет найти наибольний общий целый делитель.
    :param m: целое положительное число
    :param n: целое положительное число
    :return: наибольший общий целый делитель
    """
    if m < n:
        m, n = n, m
    while True:
        m = m % n
        if m == 0:
            return n
        n = n % m
        if n == 0:
            return m
