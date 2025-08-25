def max_pairwise(seq):
    n = len(seq)
    if 2>n>2*10^5:
        raise ValueError
    elif len(seq)!= n:
        raise ValueError
    else:
        ordenados = sorted(seq, reverse=True)
        return ordenados[0]*ordenados[1]

def max_pairwise_product_slow(numbers):
    max_product = 0
    n = len(numbers)
    for i in range(n):
        for j in range(i + 1, n):
            max_product = max(max_product, numbers[i] * numbers[j])
    return max_product

# Fast version (maybe buggy)
def max_pairwise_product_fast(numbers):
    n = len(numbers)
    index1 = max(range(n), key=lambda i: numbers[i])
    max1 = numbers[index1]
    numbers[index1] = -1
    max2 = max(numbers)
    return max1 * max2


if __name__ == "__main__":
    print("Please enter input:")
    n = int(input()) # Convert n to int
    seq = list(map(int, input().split()))
    print(max_pairwise(n, seq))

