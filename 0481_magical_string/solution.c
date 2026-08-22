// LeetCode 0481 - Magical String
// https://leetcode.com/problems/magical-string/

#include <stdlib.h>

int magicalString(int n) {
    if (n == 0) {
        return 0;
    }
    int capacity = n + 32;
    int* seq = (int*)malloc((size_t)capacity * sizeof(int));
    seq[0] = 1;
    seq[1] = 2;
    seq[2] = 2;
    int size = 3;
    int index = 2;
    while (size < n) {
        if (seq[index] == 1) {
            if (size >= capacity) {
                capacity *= 2;
                seq = (int*)realloc(seq, (size_t)capacity * sizeof(int));
            }
            seq[size++] = seq[size - 1] == 2 ? 1 : 2;
        } else {
            int value = seq[size - 1] == 2 ? 1 : 2;
            if (size + 1 >= capacity) {
                capacity *= 2;
                seq = (int*)realloc(seq, (size_t)capacity * sizeof(int));
            }
            seq[size++] = value;
            seq[size++] = value;
        }
        index++;
    }
    int ones = 0;
    for (int i = 0; i < n; i++) {
        if (seq[i] == 1) {
            ones++;
        }
    }
    free(seq);
    return ones;
}
