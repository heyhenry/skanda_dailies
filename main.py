import tkinter as tk

window = tk.Tk()
window.title("Skandailies")

# variables
money_accum = 0
is_checked = tk.IntVar()
bal = tk.StringVar(value=0)

# functions
# daily bosses
def daily_balrog():
    global money_accum
    if is_checked.get() == 1:
        money_accum += 1
        bal.set(money_accum)

def daily_zakum():
    global money_accum
    if is_checked.get() == 1:
        money_accum += 1
        bal.set(money_accum)

def daily_magnus():
    global money_accum
    if is_checked.get() == 1:
        money_accum += 1
        bal.set(money_accum)

def daily_hilla():
    global money_accum
    if is_checked.get() == 1:
        money_accum += 1
        bal.set(money_accum)

def daily_omnicln():
    global money_accum
    if is_checked.get() == 1:
        money_accum += 1
        bal.set(money_accum)

def daily_papulatus():
    global money_accum
    if is_checked.get() == 1:
        money_accum += 1
        bal.set(money_accum)

def daily_pierre():
    global money_accum
    if is_checked.get() == 1:
        money_accum += 1
        bal.set(money_accum)

def daily_vonbon():
    global money_accum
    if is_checked.get() == 1:
        money_accum += 1
        bal.set(money_accum)

def daily_crimsonqueen():
    global money_accum
    if is_checked.get() == 1:
        money_accum += 1
        bal.set(money_accum)

def daily_vellum():
    global money_accum
    if is_checked.get() == 1:
        money_accum += 1
        bal.set(money_accum)

def daily_vonleon():
    global money_accum
    if is_checked.get() == 1:
        money_accum += 1
        bal.set(money_accum)

def daily_horntail():
    global money_accum
    if is_checked.get() == 1:
        money_accum += 1
        bal.set(money_accum)

def daily_arkarium():
    global money_accum
    if is_checked.get() == 1:
        money_accum += 1
        bal.set(money_accum)

def daily_pinkbean():
    global money_accum
    if is_checked.get() == 1:
        money_accum += 1
        bal.set(money_accum)

def daily_ranmaru():
    global money_accum
    if is_checked.get() == 1:
        money_accum += 1
        bal.set(money_accum)

def daily_julieta():
    global money_accum
    if is_checked.get() == 1:
        money_accum += 1
        bal.set(money_accum)

# general bal


# content
content = tk.Frame(window).grid(row=0, column=0)

player_name_lbl = tk.Label(content, text="Player Name: ExampleHero", padx=10, pady=5).grid(row=0, column=0)
bal_lbl = tk.Label(content, text="Balance: ").grid(row=0, column=1)
bal_display_lbl = tk.Label(content, textvariable=bal, padx=10).grid(row=0, column=2)

boss_dailies = tk.Label(content, text="Boss Dailies: ", padx=10, pady=5).grid(row=1, column=0)
balrog_daily = tk.Checkbutton(content, text="Balrog", variable=is_checked, command=daily_balrog).grid(row=2, column=0)
zakum_daily = tk.Checkbutton(content, text="Zakum", variable=is_checked, command=daily_zakum).grid(row=3, column=0)
magnus_daily = tk.Checkbutton(content, text="Magnus", variable=is_checked, command=daily_magnus).grid(row=4, column=0)
hilla_daily = tk.Checkbutton(content, text="Hilla", variable=is_checked, command=daily_hilla).grid(row=5, column=0)
omnicln_daily = tk.Checkbutton(content, text="OMNI-CLN", variable=is_checked, command=daily_omnicln).grid(row=6, column=0)
papulatus_daily = tk.Checkbutton(content, text="Papulatus", variable=is_checked, command=daily_papulatus).grid(row=7, column=0)
pierre_daily = tk.Checkbutton(content, text="Pierre", variable=is_checked, command=daily_pierre).grid(row=8, column=0)
vonbon_daily = tk.Checkbutton(content, text="Von Bon", variable=is_checked, command=daily_vonbon).grid(row=9, column=0)
crimsonqueen_daily = tk.Checkbutton(content, text="Crimson Queen", variable=is_checked, command=daily_crimsonqueen).grid(row=10, column=0)
vellum_daily = tk.Checkbutton(content, text="Vellum", variable=is_checked, command=daily_vellum).grid(row=11, column=0)
vonleon_daily = tk.Checkbutton(content, text="Von Leon", variable=is_checked, command=daily_vonleon).grid(row=12, column=0)
horntail_daily = tk.Checkbutton(content, text="Horntail", variable=is_checked, command=daily_horntail).grid(row=13, column=0)
arkarium_daily = tk.Checkbutton(content, text="Arkarium", variable=is_checked, command=daily_arkarium).grid(row=14, column=0)
pinkbean_daily = tk.Checkbutton(content, text="Pink Bean", variable=is_checked, command=daily_pinkbean).grid(row=15, column=0)
ranmaru_daily = tk.Checkbutton(content, text="Ranmaru", variable=is_checked, command=daily_ranmaru).grid(row=16, column=0)
julieta_daily = tk.Checkbutton(content, text="Julieta", variable=is_checked, command=daily_julieta).grid(row=17, column=0)

window.mainloop()