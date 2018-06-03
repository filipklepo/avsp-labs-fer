import sys
import math
from collections import Counter

def l1_norm(vector):
    result = 0.0
    for dim in vector:
        result += math.sqrt(dim ** 2)
    return result

def initialize_M(adj_vertices):
    M = Counter()
    for i in range(len(adj_vertices)):
        adj_vertices_len = len(adj_vertices[i])
        for j in adj_vertices[i]:
            M[(j,i)] = 1 / adj_vertices_len
    return M

def page_rank(N, adj_vertices, beta, eps=1e-10):
    R = [1/N for i in range(N)]
    M = initialize_M(adj_vertices)
    next_R = [0 for i in range(N)]
    iteration = 1
    result = []
    while True:
        for i in range(N):
            next_R[i] = (1-beta) / N
            for j in range(N):
                next_R[i] += beta * R[j] * M[(i, j)]
        if math.fabs(l1_norm(next_R) - l1_norm(R)) < eps:
            break
        R = list(next_R)
        if iteration <= 100:
            result.append(list(next_R))
            iteration += 1
    return result

def main():
    N, beta = sys.stdin.readline().split(' ')
    N = int(N)
    beta = float(beta)
    adj_vertices = {}
    for vertex in range(N):
        adj_vertices[vertex] = []
        for adj_vertex in [int(v) for v in sys.stdin.readline().split(' ')]:
            adj_vertices[vertex].append(adj_vertex)

    queries = []
    Q = int(sys.stdin.readline())
    for q in range(Q):
        index, iter_number = [int(half) for half in sys.stdin.readline().split(' ')]
        queries.append((index, iter_number))

    res = page_rank(N, adj_vertices, beta)
    print(res)

if __name__ == '__main__':
    main()