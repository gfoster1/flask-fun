import Search


def factorial(x):
    if x == 1:
        return 1
    return x * factorial(x - 1)


if __name__ == '__main__':
    print("time to play")
    print(factorial(3))
    bubbleSort = Search.BubbleSort()
    pat = [1, 3, 2, 1, 2, 3, 1, 0, 1, 3, 4, 5]
    bubbleSort.bubble_sort(pat)
    print(pat)
    bubbleSort.binary_search(pat, 0)
