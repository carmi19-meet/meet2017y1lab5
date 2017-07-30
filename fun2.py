def draw_1d(number, a):
    for i in range(5):
        print(sym*num)

def draw_2d(num,sym, line):
    for i in range(line):
        print(sym*num)
def draw(num, line, sym, sym1):
    for i in range(line):
        for i in range(line[0], line[line]):
            print(sym*num)
        for i in range(line[1], line[line-1]):
            print(sym1*num)


def special_draw_2d(number, lines, c1, c2):
    first_line = c1*lines
    fill_line = c1+ ((lines-2)*c2) + c1
    for num in range(number):
        if num == 0 or num == number-1:
            print(first_line)
        else:
            print(fill_line)
       



            
