"""
Vérifie si une chaîne de caractère est un palindrome
"""
#### Fonction secondaire


def ispalindrome(p):

    """
    Nettoie la chainde caractère p en supprimant les espaces, accents et caractères spéciaux
    et la compare avec son inverse
    """
    p = p.lower()# chaine en majuscule
    p = p.replace(" ","")# supprime les espaces blancs

    #supprime les accents
    p = p.replace("é","e")
    p = p.replace("è","e")
    p = p.replace("ê","e")
    p = p.replace("ë","e")
    p = p.replace("à","a")
    p = p.replace("â","a")
    p = p.replace("ï","i")
    p = p.replace("î","i")
    p = p.replace("ô","o")
    p = p.replace("û","u")
    p = p.replace("ü","u")
    p = p.replace("ç","c")

    #supprime les caractères spéciaux
    clean_p = ""
    for char in p:
        if char.isalnum():
            clean_p = clean_p + char
    p = clean_p

    s = p[::-1]# on créer une chaine s qui est l'inverse de p

    if p == s:
        return True


    return False

#### Fonction principale


def main():
    """
    Fonction principale (main) qui teste la fonction
    ispalindrome()
    """
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
