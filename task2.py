import random


def main():
    spisok_slov = ['телефон', 'цепочка', 'мёд', 'сумка', 'плащ', 'мир', 'окно', 'обувь', 'кот', 'проектор', 'студент']
    slovo = random.choice(spisok_slov)
    for item in slovo:
        print('_', end=' ')
    print()
    i = 0
    list_char = []
    while i < 10:
        bukva = input()
        list_char.append(bukva)
        spisok_res = []
        for item in slovo:
            if item in list_char:
                spisok_res += item
            else:
                spisok_res += '_'
        res = ' '.join(spisok_res)
        if bukva not in slovo:
            i += 1
        print(res)
        if '_' not in spisok_res:
            print('you win!')
            break
    else:
        print('you lose')


if __name__ == '__main__':
    main()