from tkinter import *
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
import math

###   ՀԱՇՎԻՉԻ ՊԱՏՈՒՀԱՆԻ ՍԱՀՄԱՆՈՒՄ   ###
root = Tk()
root.title('TooynCalc')
root.minsize(700, 630)

###   ՓՈՓՈԽԱԿԱՆՆԵՐ ԳՈՒՅՆԵՐԻ ՀԱՄԱՐ   ###
orange = '#bf661d'
background_gray = '#323236'
entry_gray = '#5c5b5a'
button_gray = '#4a4744'

###   ԳՈՒՆԱՅԻՆ ԹԵՄԱ   ###
style = ttk.Style()
style.theme_create("nbtheme", parent="alt", settings={
    "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0]}},
    "TNotebook.Tab": {
        "configure": {"padding": [5, 1], "font": ('Helvetica', '16'),
                      "background": button_gray, "foreground": "white"},
        "map": {"background": [("selected", orange)], "expand": [("selected", [1, 3, 1, 0])]}
    }
})
style.theme_use("nbtheme")
style.configure('TFrame', background=background_gray)
tab_parent = ttk.Notebook(root)
std = ttk.Frame(tab_parent)
sci = ttk.Frame(tab_parent)
graph = ttk.Frame(tab_parent)
tab_parent.add(std, text="Standard")
tab_parent.add(sci, text="Scientific")
tab_parent.add(graph, text="Graphic")
tab_parent.pack(expand=1, fill='both')

###   ՍՏԱՆԴԱՐՏ ՌԵԺԻՄ   ###
std_entry = Entry(master=std, width=36, justify=RIGHT, fg='white', bg=entry_gray, font=('Helvetica', '20'))
std_entry.grid(row=0, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")

std_btns = np.array([
    ['←', 'C', 'x²', 'xʸ', '+'],
    ['7', '8', '9', '√', '-'],
    ['4', '5', '6', '%', '×'],
    ['1', '2', '3', '(', '÷'],
    ['.', '0', '+/-', ')', '=']
])

for i in range(5):
    std.rowconfigure(i, weight=1, minsize=40)
    for j in range(5):
        std.columnconfigure(j, weight=1, minsize=40)
        cmd = lambda x=std_btns[i][j]: calc(x, std_entry)
        if i in range(1, 5) and j in range(3):
            button = Button(
                master=std, text=str(std_btns[i][j]), command=cmd,
                fg='white', bg=orange, font=('Helvetica', '20'), width=5
            ).grid(row=i + 1, column=j, padx=5, pady=5, sticky="nsew")
        else:
            button = Button(
                master=std, text=str(std_btns[i][j]), command=cmd,
                fg='white', bg=button_gray, font=('Helvetica', '20'), width=5
            ).grid(row=i + 1, column=j, padx=5, pady=5, sticky="nsew")
std.rowconfigure(5, weight=1, minsize=40)

###   ԳԻՏԱԿԱՆ ՌԵԺԻՄ   ###
sci_entry = Entry(master=sci, width=36, justify=RIGHT, fg='white', bg=entry_gray, font=('Helvetica', '20'))
sci_entry.grid(row=0, column=0, columnspan=7, padx=5, pady=5, sticky="nsew")

sci_btns = np.array([
    ['n!', 'ₙPₚ', 'ₙCₚ', 'π', 'e', 'C', '←'],
    ['sin', 'sinh', 'x²', 'x³', 'xʸ', '|x|', 'mod'],
    ['cos', 'cosh', 'exp', '√', '(', ')', '+'],
    ['tan', 'tanh', 'logₘn', '7', '8', '9', '-'],
    ['cot', 'coth', 'lg', '4', '5', '6', '×'],
    ['arcsin', 'arctan', 'ln', '1', '2', '3', '÷'],
    ['arccos', 'arccot', ',', '.', '0', '+/-', '=']
])

for i in range(7):
    sci.rowconfigure(i, weight=1, minsize=40)
    for j in range(7):
        sci.columnconfigure(j, weight=1, minsize=40)
        cmd = lambda x=sci_btns[i][j]: calc(x, sci_entry)
        if i in range(3, 7) and j in range(3, 6):
            button = Button(
                master=sci, text=str(sci_btns[i][j]), command=cmd,
                fg='white', bg=orange, font=('Helvetica', '20'), width=5
            ).grid(row=i + 1, column=j, padx=5, pady=5, sticky="nsew")
        else:
            button = Button(
                master=sci, text=str(sci_btns[i][j]), command=cmd,
                fg='white', bg=button_gray, font=('Helvetica', '20'), width=5
            ).grid(row=i + 1, column=j, padx=5, pady=5, sticky="nsew")
sci.rowconfigure(7, weight=1, minsize=40)

###   ԳՐԱՖԻԿԱԿԱՆ ՌԵԺԻՄ   ###
graph_entry1 = Entry(master=graph, width=36, justify=RIGHT, fg='white', bg=entry_gray, font=('Helvetica', '20'))
graph_entry1.grid(row=0, column=0, columnspan=8, padx=5, pady=5, sticky="nsew")

graph_entry2 = Entry(master=graph, width=36, justify=RIGHT, fg='white', bg=entry_gray, font=('Helvetica', '20'))
graph_entry2.grid(row=1, column=0, columnspan=8, padx=5, pady=5, sticky="nsew")

graph_entry3 = Entry(master=graph, width=36, justify=RIGHT, fg='white', bg=entry_gray, font=('Helvetica', '20'))
graph_entry3.grid(row=2, column=0, columnspan=8, padx=5, pady=5, sticky="nsew")

graph_entry4 = Entry(master=graph, width=36, justify=RIGHT, fg='white', bg=entry_gray, font=('Helvetica', '20'))
graph_entry4.grid(row=3, column=0, columnspan=8, padx=5, pady=5, sticky="nsew")

graph_btns = np.array([
    ['←', 'C', 'π', 'e', 'exp', '|x|', '√', '+'],
    ['sin', 'sinh', 'arcsin', 'x', '(', ')', '∛', '-'],
    ['cos', 'cosh', 'arccos', 'x²', '7', '8', '9', '×'],
    ['tan', 'tanh', 'arctan', 'xʸ', '4', '5', '6', '÷'],
    ['cot', 'coth', 'arccot', 'lg', '1', '2', '3', '='],
    ['sec', 'sech', 'arcsec', 'ln', '.', '0', '+/-', 'view\ngraphs']
])

for i in range(6):
    graph.rowconfigure(i + 4, weight=1, minsize=40)
    for j in range(8):
        graph.columnconfigure(j, weight=1, minsize=40)
        cmd = lambda x=graph_btns[i][j]: calc(x, root.focus_get())
        if i in range(2, 6) and j in range(4, 7):
            button = Button(
                master=graph, text=str(graph_btns[i][j]), command=cmd,
                fg='white', bg=orange, font=('Helvetica', '18'), width=5, height=2
            ).grid(row=i + 4, column=j, padx=5, pady=5, sticky="nsew")
        else:
            button = Button(
                master=graph, text=str(graph_btns[i][j]), command=cmd,
                fg='white', bg=button_gray, font=('Helvetica', '18'), width=5, height=2
            ).grid(row=i + 4, column=j, padx=5, pady=5, sticky="nsew")
graph.rowconfigure(9, weight=1, minsize=40)


###   ՈՐՈՇ ՖՈՒՆԿՑԻԱՆԵՐԻ ՍԱՀՄԱՆՈՒՄՆԵՐ   ###


def sin(x): return np.sin(x)


def cos(x): return np.cos(x)


def tan(x): return np.tan(x)


def cot(x): return 1 / np.tan(x)


def sec(x): return 1 / np.cos(x)


def arccot(x): return np.pi / 2 - np.arctan(x)


def arcsec(x): return np.arccos(1 / x)


def coth(x): return np.cosh(x) / np.sinh(x)


def sech(x): return 1 / np.cosh(x)


def fact(x):
    f = 1
    if x == 0:
        return f
    elif x > 0:
        for i in range(1, x + 1):
            f = f * i
        return f


def perm(n, p):
    return fact(n) / (fact(p) * fact(n - p))


def comb(n, p):
    return fact(n) / fact(n - p)


def log(m, n):
    return math.log(n, m)


###   ՈՐՈՇ ՁԵՎԱՓՈԽՈՒԹՅՈՒՆՆԵՐ   ###


def rep(entry):
    entry = entry.replace('×', '*')
    entry = entry.replace('÷', '/')
    entry = entry.replace(')(', ')*(')
    entry = entry.replace('^', '**')
    entry = entry.replace('√', 'np.sqrt')
    entry = entry.replace('∛', 'np.cbrt')
    entry = entry.replace('arcsin', 'np.arcsin')
    entry = entry.replace('arccos', 'np.arccos')
    entry = entry.replace('arctan', 'np.arctan')
    entry = entry.replace('sinh', 'np.sinh')
    entry = entry.replace('cosh', 'np.cosh')
    entry = entry.replace('tanh', 'np.tanh')
    entry = entry.replace('lg', 'np.log10')
    entry = entry.replace('ln', 'np.log')
    entry = entry.replace('%', '/100*')
    entry = entry.replace('π', 'np.pi')
    return entry


###   ՀԱՇՎԱՐԿԻ ԵՎ ՁԵՎԱՓՈԽՈՒԹՅՈՒՆՆԵՐԻ ՀԻՄՆԱԿԱՆ ՖՈՒՆԿՑԻԱ   ###


def calc(key, mode_entry):
    entry = mode_entry.get()

    ###   = ԵՎ VIEW GRAPHS ԿՈՃԱԿՆԵՐԻ ՖՈՒՆԿՑԻՈՆԱԼՈՒԹՅՈՒՆ   ###
    if key == "=" or key == 'view\ngraphs':
        try:
            entry = entry.replace('×', '*')
            entry = entry.replace('÷', '/')
            entry = entry.replace(')(', ')*(')
            entry = entry.replace('^', '**')
            entry = entry.replace('√', 'np.sqrt')
            entry = entry.replace('∛', 'np.cbrt')
            entry = entry.replace('arcsin', 'np.arcsin')
            entry = entry.replace('arccos', 'np.arccos')
            entry = entry.replace('arctan', 'np.arctan')
            entry = entry.replace('sinh', 'np.sinh')
            entry = entry.replace('cosh', 'np.cosh')
            entry = entry.replace('tanh', 'np.tanh')
            entry = entry.replace('lg', 'np.log10')
            entry = entry.replace('ln', 'np.log')
            entry = entry.replace('%', '/100*')
            entry = entry.replace('π', 'np.pi')

            if 'e' in entry:
                rest = entry
                a = rest[:rest.find('e') + 1]
                if a.find('e') == 0 or a[a.find('e') - 1] not in 'sp':
                    a = a.replace('e', '(np.e)')
                rest = rest[rest.find('e') + 1:]
                entry = a
                while 'e' in rest:
                    a = rest[:rest.find('e') + 1]
                    rest = rest[rest.find('e') + 1:]
                    if a.find('e') == 0 or a[a.find('e') - 1] not in 'sp':
                        a = a.replace('e', '(np.e)')
                    entry = entry + a
                entry = entry + rest
            result = eval(entry)
            if result - int(result) == 0:
                result = int(result)
            if ('.' in str(result) and len(str(result)) > 17) or len(str(result)) > 16:
                result = str(format(result, '.15e'))
                while result[2] == '0':
                    result = result.replace(result[2], '')
                result = float(result)
            mode_entry.delete(0, END)
            mode_entry.insert(END, str(result))

        except Exception as ex:
            if key == '=':
                template = "{0}"
                message = template.format(type(ex).__name__, ex.args)
                if message == 'OverflowError':
                    message = '( Overflow! )'
                else:
                    message = '( Invalid Expression! )'
                mode_entry.insert(END, ' ' + message)

        ###   ԳՐԱՖԻԿՆԵՐԻ ՊԱՏՈՒՀԱՆԻ ՍԱՀՄԱՆՈՒՄ ԵՎ ԿՈՆՍՏԱՆՏ ՖՈՒՆԿՑԻԱՆԵՐԻ ԳՐԱՖԻԿՆԵՐԻ ԱՊԱՀՈՎՈՒՄ   ###
        if key == 'view\ngraphs':
            x = np.arange(-60000, 60000, 0.01)
            try:
                fig, ax = plt.subplots()
                fig.canvas.set_window_title('View Graphs')

                if len(str(graph_entry1.get())) != 0:
                    y1 = eval(rep(graph_entry1.get()))
                    if type(y1) == int or type(y1) == float:
                        y1 = y1 + x - x
                    ax.plot(x, y1)

                if len(str(graph_entry2.get())) != 0:
                    y2 = eval(rep(graph_entry2.get()))
                    if type(y2) == int or type(y2) == float:
                        y2 = y2 + x - x
                    ax.plot(x, y2)

                if len(str(graph_entry3.get())) != 0:
                    y3 = eval(rep(graph_entry3.get()))
                    if type(y3) == int or type(y3) == float:
                        y3 = y3 + x - x
                    ax.plot(x, y3)

                if len(str(graph_entry4.get())) != 0:
                    y4 = eval(rep(graph_entry4.get()))
                    if type(y4) == int or type(y4) == float:
                        y4 = y4 + x - x
                    ax.plot(x, y4)

                ax.set_xlim(-5, 5)
                ax.set_ylim(-5, 5)
                fig.set_facecolor(background_gray)
                ax.set_facecolor(button_gray)

                plt.grid(color='gray')
                ax.axhline(y=0, lw=1, color='r')
                ax.axvline(x=0, lw=1, color='r')
                plt.show()
            except:
                mode_entry.insert(END, ' ( Invalid Expression! )')

    ###   ՄՆԱՑԱԾ ԿՈՃԱԿՆԵՐԻ ՖՈՒՆԿՑԻՈՆԱԼՈՒԹՅՈՒՆ ԵՎ ԿՈՆՏԵՔՍՏԱՅԻՆ ՁԵՎԱՓՈԽՈՒԹՅՈՒՆՆԵՐ   ###
    elif key == '←':
        if len(entry) > 0:
            mode_entry.delete(0, END)
            entry = entry[:-1]
            mode_entry.insert(END, str(entry))

    elif key == "C":
        mode_entry.delete(0, END)

    elif key == 'x²':
        if len(entry) > 0:
            entry = entry + '^2'
            mode_entry.delete(0, END)
            mode_entry.insert(END, str(entry))

    elif key == 'x³':
        if len(entry) > 0:
            entry = entry + '^3'
            mode_entry.delete(0, END)
            mode_entry.insert(END, str(entry))

    elif key == 'xʸ':
        if len(entry) > 0:
            entry = entry + '^'
            mode_entry.delete(0, END)
            mode_entry.insert(END, str(entry))

    elif key == '10ˣ':
        if len(entry) > 0 and entry[-1] not in '+-×*÷/^(':
            entry = entry + '×10^'
        else:
            entry = entry + '10^'
        mode_entry.delete(0, END)
        mode_entry.insert(END, str(entry))

    elif key == '√':
        if len(entry) > 0 and entry[-1] not in '+-×*÷/^(':
            entry = entry + '×√('
        else:
            entry = entry + '√('
        mode_entry.delete(0, END)
        mode_entry.insert(END, str(entry))

    elif key == '∛':
        if len(entry) > 0 and entry[-1] not in '+-×*÷/^(':
            entry = entry + '×∛('
        else:
            entry = entry + '∛('
        mode_entry.delete(0, END)
        mode_entry.insert(END, str(entry))

    elif key == '|x|':
        if len(entry) > 0 and entry[-1] not in '+-×*÷/^(':
            entry = entry + '×abs('
        else:
            entry = entry + 'abs('
        mode_entry.delete(0, END)
        mode_entry.insert(END, str(entry))

    elif key == 'exp':
        if len(entry) > 0 and entry[-1] not in '+-×*÷/^(':
            entry = entry + '×exp('
        else:
            entry = entry + 'exp('
        mode_entry.delete(0, END)
        mode_entry.insert(END, str(entry))

    elif key == 'sin':
        if len(entry) > 0 and entry[-1] not in '+-×*÷/^(co':
            entry = entry + '×sin('
        else:
            entry = entry + 'sin('
        mode_entry.delete(0, END)
        mode_entry.insert(END, str(entry))

    elif key == 'cos':
        if len(entry) > 0 and entry[-1] not in '+-×*÷/^(':
            entry = entry + '×cos('
        else:
            entry = entry + 'cos('
        mode_entry.delete(0, END)
        mode_entry.insert(END, str(entry))

    elif key == 'tan':
        if len(entry) > 0 and entry[-1] not in '+-×*÷/^(':
            entry = entry + '×tan('
        else:
            entry = entry + 'tan('
        mode_entry.delete(0, END)
        mode_entry.insert(END, str(entry))

    elif key == 'cot':
        if len(entry) > 0 and entry[-1] not in '+-×*÷/^(':
            entry = entry + '×cot('
        else:
            entry = entry + 'cot('
        mode_entry.delete(0, END)
        mode_entry.insert(END, str(entry))

    elif key == 'sec':
        if len(entry) > 0 and entry[-1] not in '+-×*÷/^(':
            entry = entry + '×sec('
        else:
            entry = entry + 'sec('
        mode_entry.delete(0, END)
        mode_entry.insert(END, str(entry))

    elif key == 'sinh':
        if len(entry) > 0 and entry[-1] not in '+-×*÷/^(':
            entry = entry + '×sinh('
        else:
            entry = entry + 'sinh('
        mode_entry.delete(0, END)
        mode_entry.insert(END, str(entry))

    elif key == 'cosh':
        if len(entry) > 0 and entry[-1] not in '+-×*÷/^(':
            entry = entry + '×cosh('
        else:
            entry = entry + 'cosh('
        mode_entry.delete(0, END)
        mode_entry.insert(END, str(entry))

    elif key == 'tanh':
        if len(entry) > 0 and entry[-1] not in '+-×*÷/^(':
            entry = entry + '×tanh('
        else:
            entry = entry + 'tanh('
        mode_entry.delete(0, END)
        mode_entry.insert(END, str(entry))

    elif key == 'coth':
        if len(entry) > 0 and entry[-1] not in '+-×*÷/^(':
            entry = entry + '×coth('
        else:
            entry = entry + 'coth('
        mode_entry.delete(0, END)
        mode_entry.insert(END, str(entry))

    elif key == 'sech':
        if len(entry) > 0 and entry[-1] not in '+-×*÷/^(':
            entry = entry + '×sech('
        else:
            entry = entry + 'sech('
        mode_entry.delete(0, END)
        mode_entry.insert(END, str(entry))

    elif key == 'arcsin':
        if len(entry) > 0 and entry[-1] not in '+-×*÷/^(':
            entry = entry + '×arcsin('
        else:
            entry = entry + 'arcsin('
        mode_entry.delete(0, END)
        mode_entry.insert(END, str(entry))

    elif key == 'arccos':
        if len(entry) > 0 and entry[-1] not in '+-×*÷/^(':
            entry = entry + '×arccos('
        else:
            entry = entry + 'arccos('
        mode_entry.delete(0, END)
        mode_entry.insert(END, str(entry))

    elif key == 'arctan':
        if len(entry) > 0 and entry[-1] not in '+-×*÷/^(':
            entry = entry + '×arctan('
        else:
            entry = entry + 'arctan('
        mode_entry.delete(0, END)
        mode_entry.insert(END, str(entry))

    elif key == 'arccot':
        if len(entry) > 0 and entry[-1] not in '+-×*÷/^(':
            entry = entry + '×arccot('
        else:
            entry = entry + 'arccot('
        mode_entry.delete(0, END)
        mode_entry.insert(END, str(entry))

    elif key == 'arcsec':
        if len(entry) > 0 and entry[-1] not in '+-×*÷/^(':
            entry = entry + '×arcsec('
        else:
            entry = entry + 'arcsec('
        mode_entry.delete(0, END)
        mode_entry.insert(END, str(entry))

    elif key == 'logₘn':
        if len(entry) > 0 and entry[-1] not in '+-×*÷/^(':
            entry = entry + '×log('
        else:
            entry = entry + 'log('
        mode_entry.delete(0, END)
        mode_entry.insert(END, str(entry))

    elif key == 'lg':
        if len(entry) > 0 and entry[-1] not in '+-×*÷/^(':
            entry = entry + '×lg('
        else:
            entry = entry + 'lg('
        mode_entry.delete(0, END)
        mode_entry.insert(END, str(entry))

    elif key == 'ln':
        if len(entry) > 0 and entry[-1] not in '+-×*÷/^(':
            entry = entry + '×ln('
        else:
            entry = entry + 'ln('
        mode_entry.delete(0, END)
        mode_entry.insert(END, str(entry))

    elif key == 'x':
        if len(entry) > 0 and entry[-1] not in '+-×*÷/^(':
            entry = entry + '×x'
        else:
            entry = entry + 'x'
        mode_entry.delete(0, END)
        mode_entry.insert(END, str(entry))

    elif key == 'e':
        if len(entry) > 0 and entry[-1] not in '+-×*÷/^(':
            entry = entry + '×e'
        else:
            entry = entry + 'e'
        mode_entry.delete(0, END)
        mode_entry.insert(END, str(entry))

    elif key == 'π':
        if len(entry) > 0 and entry[-1] not in '+-×*÷/^(':
            entry = entry + '×π'
        else:
            entry = entry + 'π'
        mode_entry.delete(0, END)
        mode_entry.insert(END, str(entry))

    elif key == 'n!':
        if len(entry) > 0 and entry[-1] not in '+-×*÷/^(':
            entry = entry + '×fact('
        else:
            entry = entry + 'fact('
        mode_entry.delete(0, END)
        mode_entry.insert(END, str(entry))

    elif key == 'ₙPₚ':
        if len(entry) > 0 and entry[-1] not in '+-×*÷/^(':
            entry = entry + '×perm('
        else:
            entry = entry + 'perm('
        mode_entry.delete(0, END)
        mode_entry.insert(END, str(entry))

    elif key == 'ₙCₚ':
        if len(entry) > 0 and entry[-1] not in '+-×*÷/^(':
            entry = entry + '×comb('
        else:
            entry = entry + 'comb('
        mode_entry.delete(0, END)
        mode_entry.insert(END, str(entry))

    elif key == "+/-":
        if "=" in mode_entry.get():
            mode_entry.delete(0, END)
        if mode_entry.get()[0] == '-':
            mode_entry.delete(0)
        else:
            mode_entry.insert(0, "-")

    else:
        if "=" in std_entry.get():
            mode_entry.delete(0, END)
            mode_entry.insert(END, key)
        else:
            mode_entry.insert(END, key)


###   ENTER ԿՈՃԱԿԻ ՖՈՒՆԿՑԻՈՆԱԼՈՒԹՅՈՒՆ   ###


def enter_key(event):
    if tab_parent.index(tab_parent.select()) == 0:
        calc("=", std_entry)
    if tab_parent.index(tab_parent.select()) == 1:
        calc("=", sci_entry)
    if tab_parent.index(tab_parent.select()) == 2:
        calc("view\ngraphs", graph_entry4)


std_entry.bind("<Return>", enter_key)
sci_entry.bind("<Return>", enter_key)
graph_entry1.bind("<Return>", enter_key)
graph_entry2.bind("<Return>", enter_key)
graph_entry3.bind("<Return>", enter_key)
graph_entry4.bind("<Return>", enter_key)

root.mainloop()
