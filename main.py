from tkinter import *

root = Tk()
root.title("Calculator")
w, h = 304, 444
root.geometry(f"{w}x{h}")

root.config(bg="#404040")
mem = StringVar()
cur_enter = StringVar()
rl = "flat"

Label(root, textvariable=mem, font=("Segoe UI", 15), relief="flat", bg="#404040", fg="white").pack(anchor="e")
Entry(root, textvariable=cur_enter, font=("Segoe UI", 40), relief="flat", justify="right", disabledforeground="white",
      disabledbackground="#404040", state="disabled").pack(fill=BOTH)


# _____function of buttons_____
def add_mul_sub_div():
    if mem.get()[-2] == "+":
        return str(float(mem.get()[:-2]) + float(cur_enter.get()))
    elif mem.get()[-2] == "-":
        return str(float(mem.get()[:-2]) - float(cur_enter.get()))
    elif mem.get()[-2] == "✕":
        return str(float(mem.get()[:-2]) * float(cur_enter.get()))
    elif mem.get()[-2] == "÷":
        return str(float(mem.get()[:-2]) / float(cur_enter.get()))


def summation():
    if len(mem.get()) < 1:
        mem.set(cur_enter.get() + " + ")
        cur_enter.set("")
    elif mem.get()[-2] == "=":
        mem.set(cur_enter.get() + " + ")
        cur_enter.set("")
    else:
        mem.set(add_mul_sub_div() + " + ")
        cur_enter.set("")


def subtraction():
    if len(mem.get()) < 1:
        mem.set(cur_enter.get() + " - ")
        cur_enter.set("")
    elif mem.get()[-2] == "=":
        mem.set(cur_enter.get() + " - ")
        cur_enter.set("")
    else:
        mem.set(add_mul_sub_div() + " - ")
        cur_enter.set("")


def multiplication():
    if len(mem.get()) < 1:
        mem.set(cur_enter.get() + " ✕ ")
        cur_enter.set("")
    elif mem.get()[-2] == "=":
        mem.set(cur_enter.get() + " ✕ ")
        cur_enter.set("")
    else:
        mem.set(add_mul_sub_div() + " ✕ ")
        cur_enter.set("")


def division():
    if len(mem.get()) < 1:
        mem.set(cur_enter.get() + " ÷ ")
        cur_enter.set("")
    elif mem.get()[-2] == "=":
        mem.set(cur_enter.get() + " ÷ ")
        cur_enter.set("")
    else:
        mem.set(add_mul_sub_div() + " ÷ ")
        cur_enter.set("")


def equals():
    if mem.get()[-2] == "=":
        pass

    else:
        g = mem.get() + cur_enter.get() + " = "
        cur_enter.set(add_mul_sub_div())
        mem.set(g)


def clear_all():
    mem.set("")
    cur_enter.set("")


def clear():
    cur_enter.set("")


def back():
    cur_enter.set(cur_enter.get()[:-1])


def zero():
    cur_enter.set(cur_enter.get() + "0")


def one():
    cur_enter.set(cur_enter.get() + "1")


def two():
    cur_enter.set(cur_enter.get() + "2")


def three():
    cur_enter.set(cur_enter.get() + "3")


def four():
    cur_enter.set(cur_enter.get() + "4")


def five():
    cur_enter.set(cur_enter.get() + "5")


def six():
    cur_enter.set(cur_enter.get() + "6")


def seven():
    cur_enter.set(cur_enter.get() + "7")


def eight():
    cur_enter.set(cur_enter.get() + "8")


def nine():
    cur_enter.set(cur_enter.get() + "9")


# _____buttons_____
btn_frame = Frame(root, relief="flat")
btn_frame.place(x=0, y=150, width=w)
Button(btn_frame, text="%", font=("Segoe UI", "15"), relief="flat", width=6, bd=1, bg="gray",
       fg="white").grid(row=0,
                        column=0,
                        padx=1,
                        pady=1)
Button(btn_frame, text="CE", font=("Segoe UI", "15"), relief="flat", width=6, bd=1, bg="gray", fg="white",
       command=clear_all).grid(row=0,
                               column=1,
                               padx=1,
                               pady=1)
Button(btn_frame, text="C", font=("Segoe UI", "15"), relief="flat", width=6, bd=1, bg="gray", fg="white",
       command=clear).grid(row=0,
                           column=2,
                           padx=1,
                           pady=1)
Button(btn_frame, text="⬅️", font=("Segoe UI", "15"), relief="flat", width=6, bd=1, bg="gray", fg="white",
       command=back).grid(row=0,
                          column=3,
                          padx=1,
                          pady=1)

Button(btn_frame, text="⅟x", font=("Segoe UI", "15"), relief="flat", width=6, bd=1, bg="gray",
       fg="white").grid(row=1,
                        column=0,
                        pady=1,
                        padx=1)
Button(btn_frame, text="x²", font=("Segoe UI", "15"), relief="flat", width=6, bd=1, bg="gray",
       fg="white").grid(row=1,
                        column=1,
                        pady=1,
                        padx=1)
Button(btn_frame, text="√x", font=("Segoe UI", "15"), relief="flat", width=6, bd=1, bg="gray",
       fg="white").grid(row=1,
                        column=2,
                        pady=1,
                        padx=1)
Button(btn_frame, text="÷", font=("Segoe UI", "15"), relief="flat", width=6, bd=1, bg="gray", fg="white",
       command=division).grid(row=1,
                              column=3,
                              pady=1,
                              padx=1)

Button(btn_frame, text="7", font=("Segoe UI", "15"), relief="flat", width=6, bd=1, fg="white", bg="#525252",
       command=seven).grid(row=2,
                           column=0,
                           pady=1,
                           padx=1)
Button(btn_frame, text="8", font=("Segoe UI", "15"), relief="flat", width=6, bd=1, fg="white", bg="#525252",
       command=eight).grid(row=2,
                           column=1,
                           pady=1,
                           padx=1)
Button(btn_frame, text="9", font=("Segoe UI", "15"), relief="flat", width=6, bd=1, fg="white", bg="#525252",
       command=nine).grid(row=2,
                          column=2,
                          pady=1,
                          padx=1)
Button(btn_frame, text="x", font=("segoe ui", "15"), relief="flat", width=6, bd=1, fg="white", bg="gray",
       command=multiplication).grid(row=2,
                                    column=3,
                                    pady=1,
                                    padx=1)

Button(btn_frame, text="4", font=("Segoe UI", "15"), relief="flat", width=6, bd=1, fg="white", bg="#525252",
       command=four).grid(row=3,
                          column=0,
                          pady=1,
                          padx=1)
Button(btn_frame, text="5", font=("Segoe UI", "15"), relief="flat", width=6, bd=1, fg="white", bg="#525252",
       command=five).grid(row=3,
                          column=1,
                          pady=1,
                          padx=1)
Button(btn_frame, text="6", font=("Segoe UI", "15"), relief="flat", width=6, bd=1, fg="white", bg="#525252",
       command=six).grid(row=3,
                         column=2,
                         pady=1,
                         padx=1)
Button(btn_frame, text="-", font=("Segoe UI", "15"), relief="flat", width=6, bd=1, fg="white", bg="gray",
       command=subtraction).grid(
    row=3,
    column=3,
    pady=1,
    padx=1)

Button(btn_frame, text="1", font=("Segoe UI", "15"), relief="flat", width=6, bd=1, fg="white", bg="#525252",
       command=one).grid(row=4,
                         column=0,
                         pady=1,
                         padx=1)
Button(btn_frame, text="2", font=("Segoe UI", "15"), relief="flat", width=6, bd=1, fg="white", bg="#525252",
       command=two).grid(row=4,
                         column=1,
                         pady=1,
                         padx=1)
Button(btn_frame, text="3", font=("Segoe UI", "15"), relief="flat", width=6, bd=1, fg="white", bg="#525252",
       command=three).grid(row=4,
                           column=2,
                           pady=1,
                           padx=1)
Button(btn_frame, text="+", font=("Segoe UI", "15"), relief="flat", width=6, bd=1, fg="white", bg="gray",
       command=summation).grid(
    row=4,
    column=3,
    pady=1,
    padx=1)

Button(btn_frame, text="+/-", font=("Segoe UI", "15"), relief="flat", width=6, bd=1, fg="white",
       bg="gray").grid(row=5,
                       column=0,
                       pady=1,
                       padx=1)
Button(btn_frame, text="0", font=("Segoe UI", "15"), relief="flat", width=6, bd=1, fg="white", bg="#525252",
       command=zero).grid(row=5,
                          column=1,
                          pady=1,
                          padx=1)
Button(btn_frame, text=".", font=("Segoe UI", "15"), relief="flat", width=6, bd=1, fg="white",
       bg="gray").grid(row=5,
                       column=2,
                       pady=1,
                       padx=1)
Button(btn_frame, text="=", font=("Segoe UI", "15"), relief="flat", width=6, bd=1, fg="white", bg="#1D93F2",
       command=equals).grid(row=5,
                            column=3,
                            pady=1,
                            padx=1)

root.mainloop()
