import random
#from tkinter import *

#root = Tk()
#root.mainloop()


print("Игра\nКамень Ножнецы Бумага")

randomNamver = random.randint(1, 3)
if randomNamver == 1:
    figure = "Камень"
elif randomNamver == 2:
    figure = "Ножнецы"
else:
    figure = "Бумага"
print("Верите фигуру")
print("1)Камень")
print("2)Ножнецы")
print("3)Бумага")

try:
    x = int(input("Выберите фигуру \n"))
    if x == 1:
        print("")
        print("Вы выыбрали камень")
        print("Фигура противника " + str(figure))
        print("")
        if randomNamver == 1:
            print("Ничья")
        elif randomNamver == 2:
            print("Вы выграли")
        else:
            print("Вы проиграли")


    elif x == 2:
        print("")
        print("Вы выбрали Ножнецы")
        print("Фигура противника " + str(figure))
        print("")
        if randomNamver == 1:
            print("Вы проиграли")
        elif randomNamver == 2:
            print("Ничья")
        else:
            print("Вы выграли")


    elif x == 3:
        print("")
        print("Вы выыбрали Бумагу")
        print("Фигура противника " + str(figure))
        print("")
        if randomNamver == 1:
            print("Вы выграли")
        elif randomNamver == 2:
            print("Вы програли")
        else:
            print("Ничья")
    else:
        print("Пожалусто ведите 1 2 или 3")
except:
    print("Ошибка")




print()

