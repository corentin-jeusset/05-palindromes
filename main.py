#### Fonctions secondaires

modif = {
    "à": "a",
    "ä": "a",
    "â": "a",
    "ç": "c",
    "é": "e",
    "è": "e",
    "ê": "e",
    "ë": "e",
    "ï": "i",
    "î": "i",
    "ô": "o",
    "ù": "u",
    "ü": "u",
    "û": "u",
    " ": "",
    "-": "",
    ",": "",
    "'": "",
    "?": "",
    "!": "",
    ".": "",
    ":": ""
}

def orthographe(n):
    "Permet de désaccentuer les mots et de retirer la ponctuation"
    n = n.lower()
    for cle, valeur in modif.items():
        n = n.replace(cle, valeur)
    return n

def ispalindrome(p):
    "Permet de déterminer si un mot est un palindrome ou non"
    p = orthographe(p)
    for i in range (len(p) // 2):
        if p[i] != p[-i - 1]:
            return False
    return True

#### Fonction principale


def main():

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()