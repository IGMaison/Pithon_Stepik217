import time


def fib_mod(n, m):
    period = [0, 1]
    f0, f = 0, 1
    for fib_n in range(6 * m + 2):
        f0, f = f, f + f0
        mod = f % m

        if period[-2:] != [0, 1] or len(period) < 3:
            period.append(mod)
        else:
            period = period[0: -2]
            return period[n % len(period)]
    return n % m


def gcd(a, b):
    while a * b != 0:
        a, b = b, a % b
    return abs(a - b)


def nod():
    a, b = map(int, input().split())
    print(gcd(a, b))


def fib():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


def points_into_bars():
    bars, points = [], []
    for _ in range(int(input())):
        bars.append(list(map(int, input().split())))
    bars.sort(key=lambda x: x[1])
    for _ in bars:
        if points:
            if _[0] <= points[-1]:
                continue
        points.append(_[1])
    print(len(points))
    print(*points)


def backpack():
    backpack_cost = 0
    amount, volume = map(int, input().split())
    items = [list(map(int, input().split())) for _ in range(amount)]
    items.sort(key=lambda x: -x[0] / x[1])
    for item in items:
        if volume > item[1]:
            volume -= item[1]
            backpack_cost += item[0]
        else:
            backpack_cost += item[0] / item[1] * volume
            break
    return print(round(backpack_cost, 3))


def consist_of():
    n = int(input())
    num_list = [0]
    while n > num_list[-1]:
        num_list.append(num_list[-1] + 1)
        n -= num_list[-1]
    num_list[-1] += n
    print(len(num_list) - 1)
    print(*num_list[1:])
    return


def haffman():
    letters = {}
    tree = {}
    code = {}
    code_string = ''

    string = input().strip()
    for i in string:
        letters.setdefault(i, 0)
        letters[i] += 1
    letters = [[_, letters[_]] for _ in sorted(letters, key=lambda x: -letters[x])]
    if len(letters) > 1:
        while len(letters) > 1:
            temp1 = letters.pop()
            temp2 = letters.pop()
            tree[temp1[0]] = '0'
            tree[temp2[0]] = '1'
            letters.append([temp1[0] + temp2[0], temp1[1] + temp2[1]])
            letters.sort(key=lambda x: x[1], reverse=True)
    else:
        if len(letters):
            tree[letters[0][0]] = '0'

    for _ in tree:
        for __ in _:
            code[__] = tree[_] + code.setdefault(__, '')

    for _ in string:
        code_string += code[_]

    print(len(code), len(code_string))
    for _ in code:
        print(_ + ':', code.get(_))
    print(code_string)


def haffman2():
    code = {}
    words_info = list(map(int, input().split()))
    for _ in range(words_info[0]):
        temp = input().split(': ')
        code[temp[1]] = temp[0]
    words = input()
    letter_code = ''
    string_res = ''
    for _ in words:
        letter_code += _
        letter = code.get(letter_code)
        if letter:
            string_res += letter
            letter_code = ''
    print(string_res)


def insert_nomber(lst, x):
    if isinstance(lst, list) and x != '':
        x = int(x)
        lst.append(x)
        index_child = len(lst) - 1
        index_par = int((index_child + 1) / 2 - 1)
        prnt = lst[index_par]
        child = lst[index_child]
        while index_child and (child > prnt):
            lst[index_par], lst[index_child] = child, prnt
            index_child = index_par
            index_par = int((index_child + 1) / 2 - 1)
            prnt = lst[index_par]
            child = lst[index_child]
        return None
    else:
        return 'stop' if x == '' else print('неверные параметры для insert()')


def extract_max(lst):
    def child1_idx():
        return (prnt_idx + 1) * 2 - 1

    def child2_idx():
        return (prnt_idx + 1) * 2

    if len(lst) == 1:
        return lst.pop()
    elif len(lst):
        max_num = lst[0]
    else:
        return None

    lst[0] = lst.pop()
    prnt_idx = 0

    while child1_idx() <= len(lst) - 1:
        prnt = lst[prnt_idx]
        child1 = lst[child1_idx()]

        if len(lst) - 1 > child1_idx():
            child2 = lst[child2_idx()]
            if child1 > child2:
                if prnt < child1:
                    lst[prnt_idx], lst[child1_idx()] = child1, prnt
                    prnt_idx = child1_idx()
                else:
                    break
            else:
                if prnt < child2:
                    lst[prnt_idx], lst[child2_idx()] = child2, prnt
                    prnt_idx = child2_idx()
                else:
                    break
        else:
            if prnt < child1:
                lst[prnt_idx], lst[child1_idx()] = child1, prnt
                prnt_idx = child1_idx()
            else:
                break
        prnt_idx = child1_idx()
    return max_num


def priority_queue():
    heap = []
    for _ in range(int(input())):
        f = list(input().split())
        if f[0] == 'Insert':
            insert_nomber(heap, int(f[1]))
        elif f[0] == 'ExtractMax':
            print(extract_max(heap))


def bi_search():
    def find_idx(arr, item):
        if len(arr) > 1:
            start, end = 1, len(arr) - 1
            while start <= end:
                idx = (end - start) // 2 + start
                if arr[idx] == item:
                    return idx
                elif arr[idx] > item:
                    end = idx - 1
                else:
                    start = idx + 1
        if arr[1] == item:
            return 1
        else:
            return -1

    array = list(map(int, input().split()))
    data_in = list(map(int, input().split()))
    print(*[find_idx(array, _) for _ in data_in[1:]])


def inversions():
    def merge(arr):
        arr_lng = len(arr)
        inv = 0
        if arr_lng:
            new_arr = []
            idx1 = 0
            while arr_lng > 1:
                while idx1 <= arr_lng - 2:
                    idx2 = idx1 + 1
                    idx1idx = [0, len(arr[idx1])]
                    idx2idx = [0, len(arr[idx2])]
                    tmp_arr = []
                    while idx1idx[1] and idx2idx[1]:
                        if arr[idx1][idx1idx[0]] > arr[idx2][idx2idx[0]]:
                            tmp_arr.append(arr[idx2][idx2idx[0]])
                            inv += idx1idx[1]
                            idx2idx[0] += 1
                            idx2idx[1] -= 1
                        else:
                            tmp_arr.append(arr[idx1][idx1idx[0]])
                            idx1idx[0] += 1
                            idx1idx[1] -= 1
                    if idx1idx[1]:
                        for _ in arr[idx1][idx1idx[0]:idx1idx[0] + idx1idx[1]]:
                            tmp_arr.append(_)
                    else:
                        for _ in arr[idx2][idx2idx[0]:idx2idx[0] + idx2idx[1]]:
                            tmp_arr.append(_)
                    idx1 += 2
                    new_arr.append(tmp_arr)
                if arr_lng % 2:
                    new_arr.append(arr[-1])
                arr = new_arr
                new_arr = []
                arr_lng = len(arr)
                idx1 = 0
            arr.append(inv)
            return arr
        else:
            arr.append(inv)
            return arr

    input()
    print(merge(list(map(lambda x: [int(x)], input().split())))[-1])


def point_n_segment():
    import bisect
    s, p = map(int, input().split())
    head = []
    end = []
    for _ in range(s):
        a, b = map(int, input().split())
        head.append(a)
        end.append(b)
    head.sort()
    end.sort()
    for point in (map(int, input().split())):
        print(bisect.bisect(head, point) - bisect.bisect_left(end, point), end=' ')


def num_sort():
    n = input()
    arr = list(map(int, input().split()))

    def num_of_cat(num, cat):
        return num % 10 ** cat // 10 ** (cat - 1)

    def count_sort(array):
        for cat in range(1, len(str(max(arr))) + 1):
            tmp_arr = {i: 0 for i in range(10)}
            new_arr = [''] * len(arr)
            for i in array:
                tmp_arr[num_of_cat(i, cat)] += 1
            j = 0
            for i in tmp_arr:
                tmp_arr[i] = j + tmp_arr[i]
                j = tmp_arr[i]
            for i in array[::-1]:
                new_arr[tmp_arr[num_of_cat(i, cat)] - 1] = i
                tmp_arr[num_of_cat(i, cat)] -= 1
            array = new_arr
        return array

    print(*count_sort(arr))


def max_mul_seq():
    n = int(input())
    arr_in = list(map(int, input().split()))
    cnt_arr = [0 for _ in range(n)]

    for i in range(n):
        cnt_arr[i] = 1
        for j in range(i):
            if arr_in[i] % arr_in[j] == 0 and cnt_arr[j] + 1 > cnt_arr[i]:
                cnt_arr[i] = cnt_arr[j] + 1
    print(max(cnt_arr))


def max_non_increasing_seq():
    def search_max_num_of_subseq(arr, n):
        for i in range(n):
            start = 0
            end = n
            while end - start > 1:
                if max_num_of_subseq[(end + start) // 2][0] >= arr[i]:
                    start = (end + start) // 2
                else:
                    end = (end + start) // 2
            max_num_of_subseq[end] = [arr[i], i]
            arr[i] = [arr[i], max_num_of_subseq[end - 1][1]]
        return max_num_of_subseq

    def print_answ(arr, n):
        answ = []
        idx = -1
        for i in range(n, -1, -1):
            if arr[i][0] > -1:
                idx = arr[i][1]
                print(i)
                break

        while idx != '':
            answ.append(idx + 1)
            idx = arr_in[idx][1]
        print(*reversed(answ))
        return

    n = int(input())
    arr_in = list(map(int, input().split()))
    max_num_of_subseq = [[-1, ''] if x > 0 else [10 ** 6, ''] for x in range(n + 1)]

    print_answ(search_max_num_of_subseq(arr_in, n), n)


def edit_dist():
    a, b = (input(), input())
    n, m = map(len, (a, b))
    dist = [list(range(m + 1)) if j == 0 else [j, *[0] * m] for j in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            diff = int(a[i - 1] != b[j - 1])
            dist[i][j] = min(dist[i - 1][j] + 1, dist[i][j - 1] + 1, dist[i - 1][j - 1] + diff)
    print(dist[n][m])


def add_table():
    import random
    yes = 0
    no = 0
    num = [i for i in range(1, 10)]
    qty = int(input(f'Сколько примеров хотите решить?'))
    while qty > 0:
        a = random.choice(num)
        b = random.choice(num)
        try:
            answ = int(input(f'Сколько будет {a} + {b}? \n'))
            if answ == 'q':
                return
            else:
                if answ == a + b:
                    yes += 1
                    print('ВЕРНО! Молодец!')
                else:
                    no += 1
                    print(f'Неверно. Правильный ответ: {a + b}')
            qty -= 1
            print(f'Твоя оценка {(5 * yes / (yes + no)) * 10 % 100 //1 / 10} Осталось примеров ещё: {qty}шт.\n')

        except:
            print('Неверный ввод')
    return

if __name__ == "__main__":

    # fib()  #Даны целые числа 1≤n≤10^18 и 2≤m≤10^5, необходимо найти остаток от деления n-го числа Фибоначчи на m.

    # nod()  # По данным двум числам 1≤a,b≤2⋅10^9 найдите их наибольший общий делитель.

    #    points_into_bars()  # По данным n n n отрезкам необходимо найти множество точек минимального размера, для которого
    # каждый из отрезков содержит хотя бы одну из точек. В первой строке дано число 1≤n≤100
    # отрезков. Каждая из последующих n строк содержит по два числа 0≤l≤r≤10^9, задающих начало и
    # конец отрезка. Выведите оптимальное число m m m точек и сами m m m точек. Если таких множеств
    # точек несколько, выведите любое из них.

    #    backpack() #Задача на программирование: непрерывный рюкзак. Первая строка содержит количество предметов 1≤n≤10^3
    # и вместимость рюкзака 0≤W≤2⋅10^6 Каждая из следующих n строк задаёт стоимость 0≤ci≤2⋅10^6  и объём
    # 0<wi≤2⋅10^6 предмета (n, W, ci c_i ci​, wi w_i wi​ — целые числа). Выведите максимальную стоимость
    # частей предметов (от каждого предмета можно отделить любую часть, стоимость и объём при этом
    # пропорционально уменьшатся), помещающихся в данный рюкзак, с точностью не менее трёх знаков после
    # запятой.

    #    consist_of()    #По данному числу 1≤n≤10^9 найдите максимальное число k, для которого
    # n можно представить как сумму k различных натуральных слагаемых. Выведите в первой строке
    # число k, во второй — k слагаемых.

    #    haffman()#По данной непустой строке s s s длины не более 104 10^4 104, состоящей из строчных букв латинского
    #    алфавита, постройте оптимальный беспрефиксный код. В первой строке выведите количество различных букв k k k,
    #    встречающихся в строке, и размер получившейся закодированной строки. В следующих k k k строках запишите коды
    #    букв в формате "letter: code". В последней строке выведите закодированную строку.

    #   haffman2()#Восстановите строку по её коду и беспрефиксному коду символов.
    # В первой строке входного файла заданы два целых числа k k k и l l l через пробел — количество
    # различных букв, встречающихся в строке, и размер получившейся закодированной строки, соответственно.
    # В следующих k k k строках записаны коды букв в формате "letter: code". Ни один код не является
    # префиксом другого. Буквы могут быть перечислены в любом порядке. В качестве букв могут встречаться
    # лишь строчные буквы латинского алфавита; каждая из этих букв встречается в строке хотя бы один раз.
    # Наконец, в последней строке записана закодированная строка. Исходная строка и коды всех букв непусты.
    # Заданный код таков, что закодированная строка имеет минимальный возможный размер.
    # В первой строке выходного файла выведите строку s s s. Она должна состоять из строчных букв латинского
    # алфавита. Гарантируется, что длина правильного ответа не превосходит 104 10^4 104 символов.
    #    Sample
    #    Input
    #    2:
    #
    #    4
    #    14
    #    a: 0
    #    b: 10
    #    c: 110
    #    d: 111
    #    01001100100111
    #
    #    Sample
    #    Output
    #    2:
    #
    #    abacabad

    # priority_queue() #Задача на программирование: очередь с приоритетами. Первая строка входа содержит число операций
    # 1≤n≤10^5. Каждая из последующих n строк задают операцию одного из следующих двух типов:
    # Insert x, где 0≤x≤10^9 — целое число;
    # ExtractMax.
    # Первая операция добавляет число x в очередь с приоритетами, вторая — извлекает максимальное
    # число и выводит его.

    # bi_search()  # Задача на программирование: двоичный поиск В первой строке даны целое число 1≤n≤10^5 и массив
    # A[1…n] из n различных натуральных чисел, не превышающих 10^9, в порядке возрастания,
    # во второй — целое число 1≤k≤10^5 и k натуральных чисел b1,…,bk, не превышающих  10^9.
    # Для каждого i от 1 до k необходимо вывести индекс 1≤j≤n, для которого A[j]=bi A[j]=bi​, или −1,
    # если такого j нет.
    # Sample Input:
    # 5 1 5 8 12 13
    # 5 8 1 23 1 11
    # Sample Output:
    # 3 1 -1 1 -1

    # inversions() #Первая строка содержит число 1≤n≤10^5, вторая — массив A[1…n], содержащий натуральные числа,
    # не превосходящие 10^9. Необходимо посчитать число пар индексов 1≤i<j≤n, для которых A[i]>A[j].
    # (Такая пара элементов называется инверсией массива. Количество инверсий в массиве является в
    # некотором смысле его мерой неупорядоченности: например, в упорядоченном по неубыванию массиве
    # инверсий нет вообще, а в массиве, упорядоченном по убыванию, инверсию образуют каждые два элемента.)
    # Sample Input:
    # 5
    # 2 3 9 2 9
    # Sample Output:
    # 2

    # point_n_segment() #В первой строке задано два целых числа 1≤n≤50000 и 1≤m≤50000 — количество отрезков и точек
    # на прямой, соответственно. Следующие n строк содержат по два целых числа ai и bi​ (ai≤bi​)
    # — координаты концов отрезков. Последняя строка содержит m целых чисел — координаты точек.
    # Все координаты не превышают 10^8 по модулю. Точка считается принадлежащей отрезку, если она
    # находится внутри него или на границе. Для каждой точки в порядке появления во вводе выведите,
    # скольким отрезкам она принадлежит.
    # Sample Input:
    # 2 3
    # 0 5
    # 7 10
    # 1 6 11
    # Sample Output:
    # 1 0 0

    # num_sort() #Задача на программирование: сортировка подсчётом/ Первая строка содержит число 1≤n≤10^4, вторая — n
    # натуральных чисел, не превышающих 10. Выведите упорядоченную по неубыванию последовательность этих
    # чисел.
    # Sample Input:
    # 5
    # 2 3 9 2 9
    # Sample Output:
    # 2 2 3 9 9

    # max_mul_seq() #наибольшая последовательнократная подпоследовательность Дано целое число 1≤n≤10^3 и массив A[1…n]
    # натуральных чисел, не превосходящих 2⋅10^9. Выведите максимальное 1≤k≤n, для которого найдётся
    # подпоследовательность 1≤i1<i2<…<ik≤n длины k, в которой каждый элемент делится на предыдущий
    # (формально: для  всех 1≤j<k, A[ij] ∣ A[ij+1]]).
    # Sample Input:
    # 4
    # 3 6 7 12
    # Sample Output:
    # 3

    # max_non_increasing_seq() # наибольшая невозрастающая подпоследовательность. Дано целое число 1≤n≤10^5 и массив
    # A[1…n], содержащий неотрицательные целые числа, не превосходящие 10^9. Найдите
    # наибольшую невозрастающую подпоследовательность в A. В первой строке выведите её длину
    # k, во второй — её индексы 1≤i1<i2<…<ik≤n (таким образом, A[i1]≥A[i2]≥…≥A[in].
    # Sample Input:
    # 5
    # 5 3 4 4 2
    # Sample Output:
    # 4
    # 1 3 4 5

    # edit_dist() #расстояние редактирования. Вычислите расстояние редактирования двух данных непустых строк длины
    # не более 10^2, содержащих строчные буквы латинского алфавита.
    # Sample Input 1:
    # ab
    # ab
    # Sample Output 1:
    # 0
    # Sample Input 2:
    # short
    # ports
    # Sample Output 2:
    # 3

    #add_table() #программа для тренировки с ребёнком таблицы сложения.
