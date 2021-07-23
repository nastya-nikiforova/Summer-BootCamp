import math


def main():
    with open('INPUT.txt', 'r') as input_file:
        input_data = input_file.read().split('\n')
        n, m, h = map(int, input_data)
    result = math.ceil(m / (h // n))
    with open('OUTPUT.txt', 'w') as output_file:
        output_file.write(str(result))


if __name__ == '__main__':
    main()
