def average(numbers: list[float]) -> float:
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)


def greet(name: str) -> str:
    return "Xin chào, " + name


def total_length(words: list[str]) -> int:
    return sum(len(w) for w in words)
