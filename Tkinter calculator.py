from tkinter import *
from tkinter.ttk import *
import math

def factorial(y):
    """ Using """
    l = len(y)
    x = int(y[:-1])
    fac = 1
    if x == 0:
        return 1
    else:
        for n in range(1, x+1):
            fac = fac*n
        return str(fac)


def power(some_string):
    """ Takes a string containing only numbers and the ^ representing exponentiation
    and calculates the answer, returning a string"""
    ram = some_string.split('^')
    for a in ram:
        ram[ram.index(a)] = float(a)
    while len(ram) > 1:
        x = ram[-2]**ram[-1]
        ram.pop(-1)
        ram[-1] = x
    result = ''.join(map(str, ram))
    return result


def percent(some_string):
    """ Takes in a string and calculates the percentage"""
    ram = some_string.split('%')
    l = len(ram)
    for a in ram:
        ram[ram.index(a)] = float(a)
    while len(ram) > 1:
        x = ram[0] * ram[1]
        ram.pop(0)
        ram[0] = x
    h = (100**(l-1))
    ram[0] = ram[0]/h
    result = ''.join(map(str, ram))
    return result


def addition(some_string):
    """ Takes in a string and returns the sum of all the individual numbers"""
    ram = some_string.split('+')
    for a in ram:
        ram[ram.index(a)] = float(a)
    while len(ram) > 1:
        x = ram[0] + ram[1]
        ram.pop(0)
        ram[0] = x
    result = ''.join(map(str, ram))
    return result


def subtraction(some_string):
    """ Takes a string, starting from the left, subtracts the subsequent numbers"""
    if some_string[0] != '-':
        ram = some_string.split('-')
    elif some_string[0] == '-':
        ram = some_string.split('-')
        ram.pop(0)
        ram[0] = '-' + ram[0]
    for a in ram:
        ram[ram.index(a)] = float(a)
    while len(ram) > 1:
        x = ram[0]-ram[1]
        ram.pop(0)
        ram[0] = x
    result = ''.join(map(str, ram))
    return result


def multiply(some_string):
    """ Takes a string and calculates the product"""
    ram = some_string.split('*')
    for a in ram:
        ram[ram.index(a)] = float(a)
    while len(ram) > 1:
        x = ram[0]*ram[1]
        ram.pop(0)
        ram[0] = x
    result = ''.join(map(str, ram))
    return result


def divide(some_string):
    """ Takes a string containing only the division symbol and calculates the answer,
        returning a string

        In the case of multiple division symbols it works from left to right"""
    ram = some_string.split('/')
    for a in ram:
        ram[ram.index(a)] = float(a)
    while len(ram) > 1:
        x = ram[0]/ram[1]
        ram.pop(0)
        ram[0] = x
    result = ''.join(map(str, ram))
    return result


def simple_cal(some_string):
    """ Takes in a string representing an equation with no brackets. Using (B)IDMAS it calculates
      the answer to the equation. It returns a single float in string format."""
    operators = ['^', '/', '*', '%', '+', '-']
    operator_d = {'^': power, '/': divide, '*': multiply, '%': percent, '+': addition, '-': subtraction}
    for m in operators:
        eq_list = [some_string]
        if m in some_string:
            print(f"This is m: {m}")
            for x in operators[operators.index(m)+1:]:
                print(f"This is x: {x}")
                temp = list()
                list_of_y = list()
                print(f"equation list before y: {eq_list}")
                for y in eq_list:
                    print(f"This is y: {y}")
                    # Testing if there are minus symbols in the string. Minus numbers cause problems
                    # so the - symbol have to be dealt with in a different manner to normal operators.
                    if x in y and x != '-':
                        list_of_y.append(y)
                        split = y.split(x)
                        for s in split:
                            temp.append(s)
                        eq_list = eq_list + temp
                    elif x in y and x == '-':
                        if y[0] == '-' and '-' not in y[1:]:
                            continue
                        elif y[0] == '-' and '-' in y[1:]:
                            count_a = 0
                            i = []
                            list_of_y.append(y)

                            for nu in y:
                                print(nu)
                                if nu == '-' and y[count_a - 1] not in operators:
                                    i.append(count_a)
                                    count_a += 1
                                else:
                                    count_a += 1
                            temp = [y[a:b] for a, b in zip(i, i[1:] + [None])]
                            eq_list = eq_list + temp
                            print(temp)
                        elif y[0] != '-' and '-' in y[1:]:
                            count_a = 0
                            i = [0]
                            list_of_y.append(y)
                            print(f"This is list_of_y: {list_of_y}")
                            for nu in y:
                                print(nu)
                                if nu == '-' and y[count_a - 1] not in operators:
                                    i.append(count_a)
                                    count_a += 1
                                else:
                                    count_a += 1
                            print(i)
                            temp = [y[a:b] for a, b in zip(i, i[1:] + [None])]
                            print(temp)
                            eq_list = eq_list + temp
                print(f"hallo {temp}")
                for el in list_of_y:
                    eq_list.pop(eq_list.index(el))
            print(f"Printing eq_list: {eq_list}")
            count = -1
            duds = list()
            for a in eq_list:
                count += 1
                if m not in a:
                    duds.append(a)
                    continue
            for d in duds:
                eq_list.remove(d)
            print(f"final eq_list: {eq_list}")
            for b in eq_list:
                o = operator_d[m](b)
                some_string = some_string.replace(b, o)
                print(f"we got here to calcualte: {some_string}")
    return some_string


def list_duplicates_of(seq, item):
    """ Takes a string and an object and finds the index of each of the duplicates of that object
    """
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item, start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs


def every_brackets(some_string):
    """ Takes a list representing an equation and return the index of each bracket
    """
    bracket_f = list_duplicates_of(some_string, '(')
    bracket_b = list_duplicates_of(some_string, ')')
    all_brackets = bracket_f + bracket_b
    all_brackets.sort()
    return all_brackets


def one_zero(some_string):
    """ Takes a list representing and equation and returns a list of ordered 1's and 0's
    corresponding to forward and backward brackets
    """
    bracket_f = list_duplicates_of(some_string, '(')
    bracket_b = list_duplicates_of(some_string, ')')
    all_brackets = bracket_f + bracket_b
    all_brackets.sort()
    for x in bracket_f:
        if x in all_brackets:
            all_brackets[all_brackets.index(x)] = '1'
    for y in bracket_b:
        if y in all_brackets:
            all_brackets[all_brackets.index(y)] = '0'
    return all_brackets


class Equation:

    def __init__(self, equation):
        self.equation = equation
        self.left_brackets = list_duplicates_of(equation, '(')
        self.right_brackets = list_duplicates_of(equation, ')')
        self.raw = self.left_brackets + self.right_brackets
        self.raw.sort()
        self.all_brackets = self.left_brackets + self.right_brackets
        self.all_brackets.sort()
        for x in self.left_brackets:
            if x in self.all_brackets:
                self.all_brackets[self.all_brackets.index(x)] = '1'
        for y in self.right_brackets:
            if y in self.all_brackets:
                self.all_brackets[self.all_brackets.index(y)] = '0'

    def __str__(self):
        return self.equation

    def brackets(self):
        """" Produces a dictionary of pairs of index positions corresponding to pairs of enclosing
            brackets in an equation

            Keyword arguments:
            one_and_zeros - - List of 1's corresponding to forward brackets amd 0's
            corresponding to backward brackets
            list_of_brackets - - A corresponding list of the index of each of the above brackets
            """
        d = {}
        count = 0
        indexer = 0
        for m in self.all_brackets:
            if m == '1':
                count += 1
                y_indexer = indexer + 1
                for y in self.all_brackets[indexer + 1:len(self.all_brackets) + 1]:
                    if y == '1':
                        count += 1
                        y_indexer += 1
                    else:
                        count -= 1
                        if count == 0:
                            d.update({int(self.raw[indexer]): (int(self.raw[indexer]), int(self.raw[y_indexer]))})
                            indexer += 1
                            break
                        y_indexer += 1
            else:
                indexer += 1
                continue
        return d


def calculator(some_string):
    """ Takes in a string representing any equations involving the operators (, ), x, /, -, +, %, ^ and calculates
     the resultm, returning it as a string"""
    equ = Equation(some_string)
    answer = equ.equation
    left = equ.left_brackets
    d = equ.brackets()  # d is a Dictionary of the indexes of each bracket pair
    count = 1
    p = {}  # dictionary to store a key and a filler that is the same length of the removed segment of the equation
    q = {}  # Dictionary to store a matching key with the piece of equation that has been replaced with filler
    for le in left[::-1]:
        print(f"------- this is l {le}")
        print(d)
        x, y = d[le]  # Setting x, y to be the indexes of a pair of brackets that the code is now calculating
        print(x, y)
        size = len(answer[x: y+1])
        if x == 0 and answer[x] == '(':  # This case is only triggered when the out-most bracket is at the index 0.
            temp_answer = answer[x+1: y]
            ks = list_duplicates_of(temp_answer, 'K')  # Setting up a list to record the positions of all K's
            # representing the section fo the equation that have been chenged
            print(temp_answer)
            print(f"ks: {ks}")
            for k in ks:  # Replacin
                temp_answer = temp_answer.replace(p[f"K{answer[int(k) + 2]}"],
                                                  q[f"K{answer[int(k) + 2]}"])
            temp = simple_cal(temp_answer)
            answer = answer.replace(answer[x: y+1], temp)
            print(answer)
            print(f"This is answer2: {answer}")
            break
        elif 'K' not in answer[x: y+1]:
            temp = simple_cal(answer[x + 1: y])
            q.update({f'K{count}': temp})
            waz = size - len(str(count)) - 1
            filler = f'K{count}' + '_'*waz
            p.update({f'K{count}': filler})
            answer = answer.replace(answer[x: y+1], filler)
            count += 1
            print(f"This is answer1: {answer}")
        else:
            temp_answer = answer[x+1: y]
            print(temp_answer)
            while 'K' in temp_answer:
                temp_answer = temp_answer.replace(p[f"K{temp_answer[temp_answer.index('K')+1]}"],
                                                  q[f"K{temp_answer[temp_answer.index('K')+1]}"])
            temp = simple_cal(temp_answer)
            q.update({f'K{count}': temp})
            waz = size - len(str(count)) - 1
            filler = f'K{count}' + '_' * waz
            p.update({f'K{count}': filler})
            answer = answer.replace(answer[x: y + 1], filler)
            count += 1
            print(f"This is answer3: {answer}")
    while 'K' in answer:
        answer = answer.replace(p[f"K{answer[answer.index('K')+1]}"],
                                q[f"K{answer[answer.index('K')+1]}"])
    answer = simple_cal(answer)

    return answer


class Example(Frame):

    def __init__(self):
        self.old_equation = 'last equation'
        super().__init__()

        self.initUI()
        self.ans = 0


    def initUI(self):

        self.master.title("Scientific Calculator")
        normal_font = ('Verdana', 20)
        large_font = ('Verdana', 40)

        style = Style()
        style.configure("TButton", padding=(10, 15, 10, 15),
                          font=normal_font)
        #style2 = Style()
        #style2.configure("LButton", bg='blue', padding=(10, 15, 10, 15), font=normal_font)

        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.columnconfigure(3, pad=3)

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)
        self.rowconfigure(4, pad=3)

        def button_click(number):
            l = len(display.get())
            display.insert(l+1, number)
            return

        def button_wipe():
            l = len(display.get())
            display.delete(l-1)

        def converter(some_string):
            if '--' in some_string:
                some_string = some_string.replace('--', '+')
            for x in some_string:
                if x == 'x':
                    some_string = some_string.replace('x', '*')
                if x == 'π':
                    some_string = some_string.replace('π', '3.1415926535')
                if x == 'e':
                    some_string = some_string.replace('e', '2.7182818284')

            return some_string

        def errorx(some_string):
            eq = Equation(some_string)
            alphabetz = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                        'u', 'v', 'w', 'x', 'y', 'z']
            numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', 'e', 'π']
            if len(eq.left_brackets) != len(eq.right_brackets):
                return True
            for char in some_string:
                if char in numbers:
                    continue
                elif char in alphabetz:
                    return True

        def is_number_tryexcept(s):
            """ Returns True is string is a number. """
            try:
                float(s)
                return True
            except ValueError:
                return False

        def fac_sort(some_string):
            count = -1
            fac_ind = []
            operators = ['^', '/', '*', '%', '+', '-']
            for x in some_string[::-1]:
                if x == '!':
                    fac_ind.append(count)
                    count -= 1
                else:
                    count -= 1
            refine = some_string[0: fac_ind[0]]
            refine_list = refine.split('!')
            refine_list_2 = []
            for r in refine_list:
                print(r)
                if is_number_tryexcept(r):
                    refine_list_2.append(r + '!')
                else:
                    count_a = -1
                    for f in r[::-1]:
                        if f in operators:
                            refine_list_2.append(r[count_a + 1::] + '!')
                        else:
                            count_a -= 1
            answer = some_string
            for a in refine_list_2:
                answer = answer.replace(a, str(math.gamma(float(a[:-1]) + 1)))
            return answer

        def equals():
            j = len(old_eq.get())
            print(errorx(display.get()))
            if errorx(converter(display.get())):
                display.delete(0, 'end')
                display.insert(0, 'ERROR')
            else:
                old_eq.config(state='write')
                self.old_equation = display.get() + '='
                old_eq.delete(0, j+1)
                old_eq.insert(0, self.old_equation)
                old_eq.config(state='readonly')
                dis = converter(display.get())
                if '!' in dis:
                    dis = fac_sort(dis)
                print(dis)
                l = len(display.get())
                display.delete(0, l+1)
                display.insert(0, calculator(dis))
                self.ans = display.get()

        def AC():
            l = len(display.get())
            display.delete(0, l+1)



        old_eq = Entry(self)
        old_eq.grid(row=6, column=3, columnspan=3, sticky=W+E)
        old_eq.insert(0, self.old_equation)
        old_eq.config(state='readonly')
        #text = Text(self, height=10, width=10)
        #text.pack(padx=5, pady=3)
        #text.insert('Previous Equation')
        display = Entry(self, font=large_font)
        display.grid(row=0, columnspan=6, sticky=W + E)

        button0 = Button(self, text='0', command=lambda: button_click(0))
        button0.grid(row=5, column=2)
        button1 = Button(self, text='1', command=lambda: button_click(1))
        button1.grid(row=4, column=2)
        button2 = Button(self, text='2', command=lambda: button_click(2))
        button2.grid(row=4, column=3)
        button3 = Button(self, text='3', command=lambda: button_click(3))
        button3.grid(row=4, column=4)
        button4 = Button(self, text='4', command=lambda: button_click(4))
        button4.grid(row=3, column=2)
        button5 = Button(self, text='5', command=lambda: button_click(5))
        button5.grid(row=3, column=3)
        button6 = Button(self, text='6', command=lambda: button_click(6))
        button6.grid(row=3, column=4)
        button7 = Button(self, text='7', command=lambda: button_click(7))
        button7.grid(row=2, column=2)
        button8 = Button(self, text='8', command=lambda: button_click(8))
        button8.grid(row=2, column=3)
        button9 = Button(self, text='9', command=lambda: button_click(9))
        button9.grid(row=2, column=4)

        b_pi = Button(self, text='π', command=lambda: button_click('π'))
        b_pi.grid(row=5, column=0)
        b_e = Button(self, text='e', command=lambda: button_click('e'))
        b_e.grid(row=4, column=0)
        bb3 = Button(self)
        bb3.grid(row=3, column=0)
        bb4 = Button(self)
        bb4.grid(row=2, column=0)
        b_ans = Button(self, text='ANS', command=lambda: button_click(self.ans))
        b_ans.grid(row=1, column=0)
        b_percent = Button(self, text='%', command=lambda: button_click('%'))
        b_percent.grid(row=5, column=1)
        b_power = Button(self, text='x^y', command=lambda: button_click('^'))
        b_power.grid(row=4, column=1)
        b_factorial = Button(self, text='x!', command=lambda: button_click('!'))
        b_factorial.grid(row=3, column=1)
        bb9 = Button(self)
        bb9.grid(row=2, column=1)
        bb10 = Button(self)
        bb10.grid(row=1, column=1)

        b_point = Button(self, text='.', command=lambda: button_click('.'))
        b_equals = Button(self, text='=', command=lambda: equals())

        b_plus = Button(self, text='+', command=lambda: button_click('+'))
        b_minus = Button(self, text='-', command=lambda: button_click('-'))
        b_times = Button(self, text='x', command=lambda: button_click('x'))
        b_divide = Button(self, text='÷', command=lambda: button_click('/'))
        b_del = Button(self, text='del', command=lambda: button_wipe())
        b_del.grid(row=1, column=4)
        b_ac = Button(self, text='AC', command=lambda: AC())
        b_ac.grid(row=1, column=5)
        b_leftb = Button(self, text='(', command=lambda: button_click('('))
        b_rightb = Button(self, text=')', command=lambda: button_click(')'))

        b_point.grid(row=5, column=3)
        b_equals.grid(row=5, column=4)
        b_plus.grid(row=5, column=5)
        b_minus.grid(row=4, column=5)
        b_times.grid(row=3, column=5)
        b_divide.grid(row=2, column=5)

        b_leftb.grid(row=1, column=2)
        b_rightb.grid(row=1, column=3)

        self.pack()


def main():

    root = Tk()
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
