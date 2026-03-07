
GALLOWS_STAGES = {
    6: """
    _______
    |     |
    |
    |
    |
    |
    """,
    5: """
    _______
    |     |
    |     O
    |
    |
    |
    """,
    4: """
    _______
    |     |
    |     O
    |     |
    |
    |
    """,
    3: """
    _______
    |     |
    |     O
    |    /|
    |
    |
    """,
    2: """
    _______
    |     |
    |     O
    |    /|\\
    |
    |
    """,
    1: """
    _______
    |     |
    |     O
    |    /|\\
    |    /
    |
    """,
    0: """
    _______
    |     |
    |     O
    |    /|\\
    |    / \\
    |
    """
}

# Для удобства можно добавить и обратный порядок
GALLOWS_BY_ATTEMPTS = {
    6: GALLOWS_STAGES[6],  # 6 попыток осталось - пустая виселица
    5: GALLOWS_STAGES[5],
    4: GALLOWS_STAGES[4],
    3: GALLOWS_STAGES[3],
    2: GALLOWS_STAGES[2],
    1: GALLOWS_STAGES[1],
    0: GALLOWS_STAGES[0],  # 0 попыток - полная виселица
}

def get_gallows(attempts_left):
    """
    Возвращает рисунок виселицы по количеству оставшихся попыток
    attempts_left: от 0 до 6
    """
    return GALLOWS_BY_ATTEMPTS.get(attempts_left, GALLOWS_BY_ATTEMPTS[6])

def print_gallows(attempts_left):
    """Печатает виселицу"""
    print(get_gallows(attempts_left))

