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
    r = m % n
    while m % n > 0:
        m = n
        n = r
        r = m % n
    return n
