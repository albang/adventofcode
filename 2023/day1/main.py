def exo1():
    with open("input.txt","r") as text:
        strings = [line.strip("\n") for line in text.readlines()]
    cpt=0
    int_list=[ str(x) for x in range(0,10) ]

    for line in strings:
        tmp_liste = []
        for char in line:
            if char in int_list:
                tmp_liste.append(int(char))

    #    if len(tmp_liste) >= 2:
        cpt += tmp_liste[0]*10+tmp_liste[-1]

    print(cpt)



str_to_int = [("one","1"),("two","2"),("three","3"),("four","4"),( "five","5"),( "six","6"),( "seven","7"), ("eight","8"),( "nine","9")]
def convert_str_to_int(input):
    for numero in str_to_int:
        input = input.replace(numero[0],f"{numero[0]}{numero[1]}{numero[0]}")
    return input
def exo2():
    with open("input2.txt","r") as text:
        strings = [line.strip("\n") for line in text.readlines()]
    cpt=0
    int_list=[ str(x) for x in range(0,10) ]
    for line in strings:
        tmp_liste = []
        for char in convert_str_to_int(line):
            if char in int_list:
                tmp_liste.append(int(char))
        cpt += tmp_liste[0]*10+tmp_liste[-1]
    print(cpt)


if __name__ == "__main__":
    #exo1()
    exo2()