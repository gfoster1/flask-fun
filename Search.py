class BubbleSort:
    def __init__(self):
        print("playing with classes")

    @staticmethod
    def bubble_sort(l):
        print("sorting starting")
        k = len(l)
        for i in range(k):
            for j in range(i + 1, k):
                print(f'sort i = {i} j = {j}')
                if l[i] > l[j]:
                    print("swap")
                    temp = l[i]
                    l[i] = l[j]
                    l[j] = temp
        print("sorting complete")

    @staticmethod
    def binary_search(self, l, val):
        print("searching")
        return self._binary_search(l, val, 0)

    @staticmethod
    def _binary_search(self, l, val, current_pos):
        print(f'do stuff')
        k = int(len(l) / 2)
        if l[k] < val:
            print(f'less than')
            return self._binary_search(l[0:k], val, k)
        elif l[k] > val:
            print(f'greater than')
            return self._binary_search(l[k:], val, k)
        else:
            print(f'found it')
            return k + current_pos
        return -1
