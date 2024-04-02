def find_acronym():
    look_up = input("What software acronym you want to look up?\n")

    found = False
    try:
        with open('acronyms.txt') as file:
            for line in file:
                if look_up in file:
                    print(line)
                    found = True
                    break
    except FileNotFoundError as e:
        print('File not found')
        return

    if not found:
        print('The acronym does not exists')
        
def add_acronym():
    acronym = input("What acronym do you want to add?\n")
    definition = input("What is the definition?\n")
    with open('acronyms.txt', 'a') as file:
        file.write(acronym + ' - ' + definition + '\n')

def main():
    choice = input('Do you want to Find(F) or Add(A) a acronym? ')
    if choice == 'F':
        find_acronym()
    elif choice == 'A':
        add_acronym()


main()