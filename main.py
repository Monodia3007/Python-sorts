from BogoSort import *
from MergeSort import merge_sort


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print("Which sort do you want to use ?\n1) Bogo sort\n2) Merge sort")
    answer = int(input("Réponse : "))
    print("Quelle taille de liste voulez vous ?")
    size = int(input("Taille : "))
    if answer == 1:
        bogosort(randomlist(size))
    elif answer == 2:
        merge_sort(size)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
