def yes_no_question(question) -> bool:
    print(question + " oui (y) ou non (n) : ")
    user_input = input().lower()
    if (len(user_input) != 1 and (user_input not in ['y', 'n'])):
        print("Entrée invalide, veuillez entrer y pour oui ou n pour non ")
        return yes_no_question(question)
    return user_input == 'y'

def correct_str_input() -> str:
    user_input = input()
    if (len(user_input) == 0):
        print("Aucune entrée, trouvée. Entrez à nouveau : ")
        return correct_str_input()
    elif (user_input.isdigit()):
        print("Entrée invalide, veuillez entrer une chaîne de character : ")
        return correct_str_input()
    
    return user_input
    
def correct_int_input() -> int:
    user_input = input()
    if (len(user_input) == 0):
        print("Aucune entrée, trouvée. Entrez à nouveau : ")
        return correct_int_input()
    elif (not user_input.isdigit()):
        print("Entrée invalide, veuillez entrer un nombre : ")
        return correct_int_input()
    
    return user_input
    
