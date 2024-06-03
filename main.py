import tkinter as tk

window = tk.Tk()
window.title("Skanda Dailies")

content = tk.Frame(window).grid(row=0, column=0)

money_accum = 0
bal = tk.IntVar()

def add_ursus(m : int):
    global money_accum
    money_accum += m
    # bal.set(money_accum)

def check_bal():
    print(money_accum)
    # print(bal.get())

player_name_lbl = tk.Label(content, text="Player Name: GreatHero", padx=10, pady=5).grid(row=0, column=0, columnspan=2)

arcane_lbl = tk.Label(content, text="Daily Type: Arcane River Dailies", padx=10, pady=5).grid(row=1, column=0)
vj_cb = tk.Checkbutton(content, text="Vanishing Journey", offvalue=0, onvalue=1).grid(row=2, column=0)
chuchu_cb = tk.Checkbutton(content, text="Chu Chu Island", offvalue=0, onvalue=1).grid(row=3, column=0)
lach_cb = tk.Checkbutton(content, text="Lachelain", offvalue=0, onvalue=1).grid(row=4, column=0)
arcana_cb = tk.Checkbutton(content, text="Arcana", offvalue=0, onvalue=1).grid(row=5, column=0)
morass_cb = tk.Checkbutton(content, text="Morass", offvalue=0, onvalue=1).grid(row=6, column=0)
esfera_cb = tk.Checkbutton(content, text="Esfera", offvalue=0, onvalue=1).grid(row=7, column=0)

money_lbl = tk.Label(content, text="Daily Type: Money Dailies", padx=10, pady=5).grid(row=1, column=1)
ursus_cb = tk.Checkbutton(content, text="Ursus", variable=bal,).grid(row=2, column=1)
mt_cb = tk.Checkbutton(content, text="Maple Tour", offvalue=0, onvalue=1).grid(row=3, column=1)

bal_check = tk.Button(content, text='Check Bal', command=check_bal).grid(row=0, column=2)


window.mainloop()