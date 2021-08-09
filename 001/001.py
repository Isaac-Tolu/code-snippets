# I saw this on the Exercism community.
# After spending hours thinking of how to get if statements right,
# You can imagine how I felt when I saw this solution.

def convert(number: int) -> str:
    sounds = [(3, "Pling"), (5, "Plang"), (7, "Plong")]
    result = [sound for divisor, sound in sounds if number % divisor == 0]
    return "".join(result) or f"{number}"