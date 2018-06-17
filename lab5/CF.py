import sys
from decimal import Decimal, ROUND_HALF_UP
from math import sqrt

def avg_rating_uu(ratings, i, j, k):
    cands = []
    for pos in range(len(ratings[0])):
        if pos == j:
            continue
        if ratings[i][pos] != 0:
            cands.append((pos))

    avg_ref, zeroes_ref = 0.0, 0
    for cur_i in range(len(ratings)):
        if ratings[cur_i][j] != 0:
            avg_ref += ratings[cur_i][j]
        else:
            zeroes_ref += 1
    avg_ref /= len(ratings) - zeroes_ref

    similarities_found = []
    for cand_i in range(len(cands)):
        avg_cand, zeroes_cand, cur_similarity, common_ratings = 0, 0, 0, []
        for cur_i in range(len(ratings)):
            ref_rating, cand_rating = ratings[cur_i][j], ratings[cur_i][cands[cand_i]]
            if cand_rating != 0:
                if ref_rating != 0:
                    common_ratings.append((ref_rating, cand_rating))
                avg_cand += cand_rating
            else:
                zeroes_cand += 1
        avg_cand /= len(ratings) - zeroes_cand
        for cr_ref, cr_cand in common_ratings:
            cur_similarity += (cr_ref - avg_ref) * (cr_cand - avg_cand)
        ref_denom, cand_denom = 0, 0
        for cur_i in range(len(ratings)):
            if ratings[cur_i][j] != 0:
                ref_denom += (ratings[cur_i][j] - avg_ref) ** 2
            if ratings[cur_i][cands[cand_i]] != 0:
                cand_denom += (ratings[cur_i][cands[cand_i]] - avg_cand) ** 2
        cur_similarity /= sqrt(ref_denom * cand_denom)
        similarities_found.append((cands[cand_i], cur_similarity))

    similarities_found = sorted(similarities_found, key=lambda x: x[1], reverse=True)[:k]
    similarities_found = list(filter(lambda x: x[1] > 0, similarities_found))
    avg_rating = [rating * ratings[i][val_j] for (val_j, rating) in similarities_found]
    avg_rating = sum(avg_rating) / sum(list(map(lambda x: x[1], similarities_found)))
    return avg_rating

def main():
    N, M = map(int, sys.stdin.readline().split(' '))
    ratings = []

    for i in range(N):
        ratings.append(list(map(lambda x: int(x) if x != 'X' else 0, sys.stdin.readline().rstrip('\n').split(' '))))

    Q = int(sys.stdin.readline())
    for i in range(Q):
        I, J, T, K = map(int, sys.stdin.readline().split(' '))
        if T == 1: #user-user
            print(Decimal(Decimal(avg_rating_uu(ratings, I-1, J-1, K)).quantize(Decimal('.001'), rounding=ROUND_HALF_UP)))
        else: #item-item
            #TODO !
            pass

if __name__ == '__main__':
    main()