import sys
import re
import hashlib

def calculate_simhash(text):
    sh = [0] * 128
    units = re.sub('[\s+]', ' ', text.strip()).split()
    for unit in units:
        unit_hash_bits = _hex_str_to_bin_str(_generate_unit_hash(unit))
        for i in range(128):
            sh[i] += 1 if unit_hash_bits[i] == '1' else -1
    for i in range(128):
        sh[i] = '1' if sh[i] >= 0 else '0'
    sh_hex_nibbles = [''.join(sh[x:x+4]) for x in range(0, 128, 4)]
    return ''.join([hex(int(x, 2))[2:] for x in sh_hex_nibbles])

def find_similar_docs(simhashes, query_index, max_hamming_distance):
    similar_docs = []
    query_simhash = simhashes[query_index]
    for i in range(len(simhashes)):
        if i == query_index:
            continue
        if _hamming_distance(query_simhash, simhashes[i]) <= max_hamming_distance:
            similar_docs.append(simhashes[i])
    return similar_docs

def _generate_unit_hash(unit):
    return hashlib.md5(unit.encode('utf-8')).hexdigest()

def _hamming_distance(hex1, hex2):
    bin_hex1, bin_hex2 = _hex_str_to_bin_str(hex1), _hex_str_to_bin_str(hex2)
    distance = 0
    for i in range(len(bin_hex1)):
        if bin_hex1[i] != bin_hex2[i]:
            distance += 1
    return distance

def _hex_str_to_bin_str(str):
    binary_length = len(str) * 4
    binary_value = bin(int(str, 16))[2:]
    return ''.join(['0' for i in range(binary_length - len(binary_value))]) + binary_value

if __name__ == "__main__":
    simhashes = []
    N = int(sys.stdin.readline())
    while N > 0:
        simhashes.append(calculate_simhash(sys.stdin.readline()))

        N -= 1
    Q = int(sys.stdin.readline())
    while Q > 0:
        query_data = sys.stdin.readline().split(' ')
        query_index = int(query_data[0])
        max_hamming_distance = int(query_data[1])
        print(len(find_similar_docs(simhashes, query_index, max_hamming_distance)))
        Q -= 1