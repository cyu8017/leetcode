// LeetCode 1562 - Find Latest Group of Size M
// https://leetcode.com/problems/find-latest-group-of-size-m/

#include <stdlib.h>

int findLatestStep(int* arr, int arrSize, int m) {
    if (m == arrSize) return m;
    int* lengths = (int*)calloc((size_t)arrSize + 2, sizeof(int));
    int answer = -1;
    for (int step = 1; step <= arrSize; step++) {
        int x = arr[step - 1];
        int left = lengths[x - 1], right = lengths[x + 1];
        int size = left + 1 + right;
        lengths[x - left] = lengths[x + right] = size;
        if (left == m || right == m) answer = step - 1;
    }
    free(lengths);
    return answer;
}
