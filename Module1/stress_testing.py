import random
from max_pairwise import max_pairwise_product_fast, max_pairwise_product_slow

# Stress test loop
while True:
    n = random.randint(2, 10)
    numbers = [random.randint(0, 100) for _ in range(n)]
    
    result1 = max_pairwise_product_slow(numbers.copy())
    result2 = max_pairwise_product_fast(numbers.copy())

    if result1 != result2:
        print("Wrong answer detected!")
        print("Input:", numbers)
        print("Slow result:", result1)
        print("Fast result:", result2)
        break
    else:
        print("OK")
