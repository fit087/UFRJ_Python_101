# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 11:12:02 2015

@author: aluno
"""

def gallows_game():
    print ("Player one")
    #secret_word = raw_input ("The word is: ")
    secret_word = input ("The word is: ")
    secret_list = secret_word.split()
    chances = 8
    misses_letters = len(secret_list)
    list_flags = [0]*misses_letters
    while chances:
#        for letter,flag in secret_list, list_flags:
#            if flag:
##                print(letter, end = " ")
#                print letter,
#            else:
#                print "_",
        counter = 0        
        for letter in secret_list:
            print (letter)
            #if flag:
            if list_flags[counter]:
                print(letter, end = "")
                #print letter,
            else:
                print("_", end = "")
                #print "_",
            counter += 1
        print()
        chances -= 1


if __name__ == '__main__':
    gallows_game()