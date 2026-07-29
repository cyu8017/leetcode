// LeetCode 1183 - Maximum Number of Ones
// https://leetcode.com/problems/maximum-number-of-ones/

#include <stdlib.h>

static int cmpDesc(const void* a, const void* b) {
    return *(const int*)b - *(const int*)a;
}

int maximumNumberOfOnes(int width, int height, int sideLength, int maxOnes) {
    int cap = sideLength * sideLength;
    int* counts = (int*)malloc((size_t)cap * sizeof(int));
    int idx = 0;
    for (int r = 0; r < sideLength; r++) {
        for (int c = 0; c < sideLength; c++) {
            int rows = (height - r + sideLength - 1) / sideLength;
            int cols = (width - c + sideLength - 1) / sideLength;
            counts[idx++] = rows * cols;
        }
    }
    qsort(counts, (size_t)cap, sizeof(int), cmpDesc);
    int ans = 0;
    for (int i = 0; i < maxOnes; i++) ans += counts[i];
    free(counts);
    return ans;
}
