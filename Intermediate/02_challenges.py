#### Challenges ####

from operator import index
from uuid import NAMESPACE_X500


def fizzbuzz():
    for index in range(101):
        if index % 3 == 0 and index % 5 == 0:
            print("fizzbuzz")
        elif index % 3 == 0:
            print("fizz")
        elif index % 5 == 0:
            print("buzz")
        else:
            print(index)


fizzbuzz()

def is_anagram(word1, word2):
    if word1 == word2:
        return False

    return sorted(word1.lower()) == sorted(word2.lower())


print(is_anagram("Amor", "Amor"))


def fibonacci():
    prev, next = 0 , 1

    for index in range(0, 50):

        #print(prev)

        fib = prev + next
        prev = next
        next = fib

fibonacci()

def is_primo():

    for number in range(1, 101):
        if number >= 2:
            is_divisible = False
            for index in range(2, number):
                if number % index == 0:
                    is_divisible = True
                    break
            if not is_divisible:
                print(number)

    return True

is_primo()


def reverse(text):
    text_len = len(text)
    reversed_text = ""
    for index in range(0, text_len):
        reversed_text += text[text_len - index - 1]
    return reversed_text

print(reverse("Hola mundo"))



