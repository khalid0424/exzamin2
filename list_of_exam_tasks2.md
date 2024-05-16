1:
    Explain the differences between tuples, lists, dictionaries, and sets in Python. Provide a use case for each data structure..
    
    Объясните различия между кортежами, списками, словарями и множествами в Python. Предоставьте вариант использования для каждой структуры данных.

2:
    The sequence consists of natural numbers and ends with the number 0. Determine the value of the largest element of the sequence. Numbers following zero do not need to be read.

    Последовательность состоит из натуральных чисел и завершается числом 0. Определите значение наибольшего элемента последовательности. Числа, следующие за нулем, считывать не нужно.
    Input data
    1
    7
    9
    0

    Output
    9 

3:
     all exact squares of natural numbers not exceeding a given number N.

    Выведите все точные квадраты натуральных чисел, не превосходящие данного числа N.
    Input data
    15

    Output
    1 4 9
Print
4:
   Given a list of numbers and the index of the element in the list k. Remove an element with index k.

    Дан список из чисел и индекс элемента в списке k. Удалите из списка элемент с индексом k.
    Input data    
    7 6 5 4 3 2 1
    2

    Output
    7 6 4 3 2 1 

5:
    In the list, all elements are different. Swap the minimum and maximum elements of this list.
    
    В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.
    Input data
    3 4 5 2 1

    Output
    3 4 1 2 5 

6:
    Cycle the elements of the list to the right (A[0] goes to place A[1], A[1] to place A[2], ..., last element goes to place A[0]).

    Циклически сдвиньте элементы списка вправо (A[0] переходит на место A[1], A[1] на место A[2], ..., последний элемент переходит на место A[0]).
    Input data
    1 2 3 4 5

    Output
    5 1 2 3 4 

7:
    Given a list of numbers. Count how many pairs of elements are in it that are equal to each other. It is believed that any two elements equal to each other form one pair that must be counted.

    Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.

    Input data                Input data
       1 2 3 2 3                1 1 1 1 1 
    Output                    Output
       2                        10

8:
    Write a Python program to find the maximum and minimum product of pairs of tuples within a given list.

    Напишите программу на Python, чтобы найти максимальное и минимальное произведение пар кортежей в заданном списке.

    The original list, tuple : [(2, 7), (2, 6), (1, 8), (4, 9)]

    Maximum and minimum product from the pairs of the said tuple of list: Максимальное и минимальное произведение пар   указанного кортежа списка:

    (36, 8)

9: 
    Given a string S consisting of N characters of the English alphabet, the task is to check if the given string is a palindrome. If the given string is a palindrome, then print “Yes“. Otherwise, print “No“.

    Дана строка S , состоящая из N символов английского алфавита, задача состоит в том, чтобы проверить, является ли данная строка палиндромом. Если данная строка является палиндромом, выведите « Да ». В противном случае выведите « Нет ».
    Input data                Input data
       ABCBA                    ABCD
    Output                    Output
       YES                       NO


10: 
    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
       (Римские цифры представлены семью различными символами  : I, V, X, L, C, D и M).

    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000

    For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
      (Например,  2пишется как II римская цифра, просто складывая две единицы. 12пишется как  XII, что просто X + II.   Число 27записывается как XXVII, то есть XX + V + II).

    Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.   Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same    principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
       (Римские цифры обычно пишутся от большей к меньшей слева направо. Однако цифра «четыре» не является цифрой «четыре» IIII. Вместо этого число четыре записывается как IV. Поскольку единица стоит перед пятеркой, мы вычитаем ее, получая четыре. Тот же принцип применим и к числу девять, которое записывается как IX. Есть шесть случаев, когда используется вычитание):

    I can be placed before V (5) and X (10) to make 4 and 9.           
       (I можно поставить перед V(5) и X(10), чтобы получилось 4 и 9).
    X can be placed before L (50) and C (100) to make 40 and 90.       
       (X можно поставить перед L(50) и C(100), чтобы получилось 40 и 90).
    C can be placed before D (500) and M (1000) to make 400 and 900.   
       (C можно поставить перед D(500) и M(1000), чтобы получить 400 и 900).
    Example 1:
        Input: s = "III"
        Output: 3
        Explanation: III = 3.
    Example 2:
        Input: s = "LVIII"
        Output: 58
        Explanation: L = 50, V= 5, III = 3.
    Example 3:
        Input: s = "MCMXCIV"
        Output: 1994
        Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.