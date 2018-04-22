import sys
import math
from collections import Counter

def pcy():
    num_baskets = int(sys.stdin.readline())
    s = float(sys.stdin.readline())
    num_slots = int(sys.stdin.readline())
    threshold =  math.floor(s * num_baskets)
    baskets = []
    items_cnt = Counter()
    A = 0
    for basket_i in range(num_baskets):
        basket = sys.stdin.readline()
        basket = [int(item) for item in basket.split(' ')]
        baskets.append(basket)
        for item in basket:
            items_cnt[item] += 1
            if items_cnt[item] == threshold:
                A += 1
    A = math.floor(A*(A-1)/2)
    print(A)

    num_dist_items = len(items_cnt.keys())
    slots = Counter()
    for basket in baskets:
        for i in range(len(basket)):
            for j in range(i+1, len(basket)):
                item_i, item_j = basket[i], basket[j]
                if items_cnt[item_i] >= threshold and items_cnt[item_j] >= threshold:
                    k = (int(item_i) * num_dist_items + item_j) % num_slots
                    slots[k] += 1

    pairs = Counter()
    for basket in baskets:
        for i in range(len(basket)):
            for j in range(i+1, len(basket)):
                item_i, item_j = basket[i], basket[j]
                if items_cnt[item_i] >= threshold and items_cnt[item_j] >= threshold:
                    k = (int(item_i) * num_dist_items + item_j) % num_slots
                    if slots[k] >= threshold:
                        pairs[tuple(sorted((item_i, item_j)))] += 1
    print(len(pairs.keys()))
    values = list(pairs.values())
    values.sort(reverse=True)
    for value in values:
        print(value)

if __name__ == '__main__':
    pcy()