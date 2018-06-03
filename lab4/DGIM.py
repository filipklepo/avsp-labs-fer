import sys

class DGIM:
    def __init__(self, N):
        self.N = N
        self.buckets = [] # list of tuples (sum of ones (pow of 2), timestamp)
        self.count = -1
        self.total = 0

    def query(self, k):
        k_timestamp = self.count - k
        num_of_ones = 0
        should_sum = False
        for i in range(len(self.buckets)):
            cur_size, cur_timestamp = self.buckets[i]
            if cur_timestamp <= k_timestamp:
                continue
            num_of_ones += cur_size if should_sum else cur_size // 2
            if not should_sum:
                should_sum = True
        return num_of_ones

    def update(self, bit):
        self.count += 1
        if len(self.buckets) > 0 and self.buckets[0][1] < self.count - self.N:
            self.total -= self.buckets[0][0]
            self.buckets = self.buckets[1:]

        if bit == '0':
            return
        self.buckets.append((1, self.count))
        self.total += 1
        self._merge()

    def _merge(self):
        last_index = len(self.buckets) - 1
        if self.__matching_buckets_cnt(last_index) < 3:
            return

        while self.__matching_buckets_cnt(last_index) == 3:
            last_index -= 2
            self.__merge_to_right(last_index)

    # Returns number of buckets with size equal to the size of bucket at given index
    def __matching_buckets_cnt(self, index):
        cnt = 1
        query_size, _ = self.buckets[index]
        for i in reversed(range(index)):
            size, _ = self.buckets[i]
            if size == query_size:
                cnt += 1
            else:
                break
        return cnt

    # Merges bucket at given index with bucket right to it
    def __merge_to_right(self, index):
        assert self.buckets[index][0] == self.buckets[index+1][0], 'Buckets are not of matching sizes'
        assert index+1 < len(self.buckets), 'Bucket to the right doesn\'t exist'
        res_count, _ = self.buckets[index]
        _, res_timestamp = self.buckets[index+1]
        res_count += self.buckets[index+1][0]
        self.buckets[index] = res_count, res_timestamp
        self.buckets = self.buckets[:index+1] + self.buckets[index+2:]

def main():
    N = int(sys.stdin.readline())
    dgim = DGIM(N)
    while True:
        line = sys.stdin.readline().rstrip()
        if line == '' or line == '\n':
            break
        elif line[0] == 'q':
            k = int(line[2:])
            print(dgim.query(k))
        else:
            for b in line:
                dgim.update(b)

if __name__ == '__main__':
    main()