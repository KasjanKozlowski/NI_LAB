#Zadania z Zestawu jedenastego ze zbioru zadań podstaw programowania w pythonie.
#Temat: Klasy

#Zadanie 1
class punkt:
    __x = 0
    __y = 0
    def wczytaj(self):
        self.__x=int(input())
        self.__y=int(input())
    def wypisz(self):
        print(self.__x)
        print(self.__y)
#Zadanie 2
class ukryta_liczba:
    __liczba=1
    def wczytaj(self):
        self.__liczba = int(input())
    def zeruj(self):
        self.__liczba = 0
#Zadanie 3
class liczba:
    __x = 0
    def wczytaj(self):
        self.__x=int(input())
    def wypisz(self):
        print(self.__x)
    def nadaj_w(self, x):
        self.__x=x
    def __abs__(self):
        y = (self.__x*self.__x)**(1/2)
        return y
#Zadanie 4
class osoba:
    __imie = ""
    __nazwisko = ""
    def __init__(self, imie, nazwisko):
        self.__imie = imie
        self.__nazwisko = nazwisko
    def wczytaj(self):
        self.__imie=input()
        self.__nazwisko = input()
    def wypisz(self):
        print(self.__imie, end=" ")
        print(self.__nazwisko)
        