def exo1():

    max_elves = {"red":12, "green":13, "blue":14 }
    cpt=0
    with open("input.txt","r") as text:
        strings = [line.strip("\n") for line in text.readlines()]

    for line in strings:
        game_id = line.split(":")[0].split(" ")[1]
        lancers = line.split(":")[1].split(";")
        max_cube = {}
        for jet in lancers:
            for lancer in jet.split(","):
                vide,number, color = lancer.split(' ')

                if max_cube.get(color,0) < int(number):
                    max_cube[color] = int(number)
        cond = True
        for key in max_elves:

            if max_cube[key]> max_elves[key]:
                cond =False
        if cond:
            cpt+=int(game_id)
    print(cpt)
str_to_int = [("one","1"),("two","2"),("three","3"),("four","4"),( "five","5"),( "six","6"),( "seven","7"), ("eight","8"),( "nine","9")]


def convert_str_to_int(input):
    for numero in str_to_int:
        input =input.replace(numero[0],f"{numero[0]}{numero[1]}{numero[0]}")

    print(input)
    return input

def exo2():


    cpt=0
    with open("input.txt","r") as text:
        strings = [line.strip("\n") for line in text.readlines()]

    for line in strings:
        game_id = line.split(":")[0].split(" ")[1]
        lancers = line.split(":")[1].split(";")
        max_cube = {}
        for jet in lancers:
            for lancer in jet.split(","):
                vide,number, color = lancer.split(' ')

                if max_cube.get(color,0) < int(number):
                    max_cube[color] = int(number)
        cond = True
        power=1
        for key in max_cube:

            power=power*max_cube[key]
        cpt+=power
    print(cpt)
str_to_int = [("one","1"),("two","2"),("three","3"),("four","4"),( "five","5"),( "six","6"),( "seven","7"), ("eight","8"),( "nine","9")]




if __name__ == "__main__":
    #exo1()
    exo2()