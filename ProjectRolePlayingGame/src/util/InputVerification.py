

def yes_no_question(question: str) -> bool:
    print(question + " oui (y) ou non (n) : ", end="")
    user_input: str = input().lower()
    if (len(user_input) != 1 and (user_input not in ['y', 'n'])):
        print("Entrée invalide, veuillez entrer y pour oui ou n pour non")
        yes_no_question(question)
    return user_input == 'y'

def correct_str_input() -> str:
    user_input: str = input()
    if (len(user_input) == 0):
        print("Aucune entrée, trouvée. Entrez à nouveau : ")
        return correct_str_input()
    elif (user_input.isdigit()):
        print("Entrée invalide, veuillez entrer une chaîne de character (lettres) : ")
        return correct_str_input()
    
    return user_input
    
def correct_int_input() -> int:
    user_input: str = input()
    if (len(user_input) == 0):
        print("Aucune entrée, trouvée. Entrez à nouveau : ")
        return correct_int_input()
    elif (not user_input.isdigit()):
        print("Entrée invalide, veuillez entrer un chiffre (ou nombre) : ")
        return correct_int_input()
    
    return int(user_input)
    
def ask_str(question, **kwargs):
    if kwargs is None:
        print("Error: no arguments fund for ask_str.")
    print("{}".format(question), end="")
    items = [(key, value) for (key, value) in kwargs.items()]
    for i in range(len(items)-1):
        print(" ({}){} ".format(items[i][0], items[i][1]), end="ou")
    print(" ({}){} : ".format(items[-1][0], items[-1][1]), end="")

    return correct_str_input()
        
