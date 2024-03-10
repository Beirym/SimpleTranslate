def is_upper(letter, lang):
    upper_alphabets = {
        'eng': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 
                'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
                'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
    }
    if letter in upper_alphabets[lang]:
        return True
    return False


eng_to_rus = {
    "a": "ф",
    "b": "и",
    "c": "с",
    "d": "в",
    "e": "у",
    "f": "а",
    "g": "п",
    "h": "р",
    "i": "ш",
    "j": "о",
    "k": "л",
    "l": "д",
    "m": "ь",
    "n": "т",
    "o": "щ",
    "p": "з",
    "q": "й",
    "r": "к",
    "s": "ы",
    "t": "е",
    "u": "г",
    "v": "м",
    "w": "ц",
    "x": "ч",
    "y": "н",
    "z": "я",
    "`": "ё",
    "~": "Ё",
    "!": "!",
    "@": "\"",
    "#": "№",
    "$": ";",
    "%": "%",
    "^": ":",
    "&": "?",
    "*": "*",
    "(": "(",
    ")": ")",
    "-": "_",
    "_": "-",
    "=": "+",
    "+": "=",
    "[": "х",
    "{": "Х",
    "]": "ъ",
    "}": "Ъ",
    "\\": "/",
    "|": "|",
    ";": "ж",
    ":": "Ж",
    "'": "э",
    "\"": "Э",
    ",": "б",
    "<": "Б",
    ".": "ю",
    ">": "Ю",
    "/": ".",
    "?": ",",
    " ": " ",
}