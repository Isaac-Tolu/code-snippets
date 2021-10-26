def convert(number: int) -> str:
    """
    Converts a number to raindrops..
    If it is a factor of 3, 5 or 7.

    Returns the number if it is not a factor.
    """

    sounds = [(3, "Pling"), (5, "Plang"), (7, "Plong")]
    result = [sound for divisor, sound in sounds if number % divisor == 0]

    return "".join(result) or f"{number}"