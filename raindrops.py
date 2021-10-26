def convert(number: int) -> str:
    sounds = [(3, "Pling"), (5, "Plang"), (7, "Plong")]
    result = [sound for divisor, sound in sounds if number % divisor == 0]
    return "".join(result) or f"{number}"