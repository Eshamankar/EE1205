import matplotlib.pyplot as plt

def calculate_y(n):
    return 2 * (n + 1) + (3 * (3 ** (n + 1) - 1)) / 2.0

def stemplot(data, highlight_index):
    for index, value in enumerate(data):
        marker = '*' if index == highlight_index else ''
        print(f'{index}\t| {value:.2f} {marker}')

def main():
    n_values = list(range(11))
    y_values = [calculate_y(n) for n in n_values]

    print("Stemplot for y(n):")
    stemplot(y_values, highlight_index=10)

    plt.stem(n_values, y_values, basefmt=' ', markerfmt='bo', linefmt='b-')
    plt.xlabel('n')
    plt.ylabel('y(n)')
    plt.title('Stemplot for y(n)')
    plt.show()

if __name__ == "__main__":
    main()

