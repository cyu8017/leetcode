// LeetCode 1051 - Height Checker
// https://leetcode.com/problems/height-checker/

#include <stdlib.h>
#include <string.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int heightChecker(int* heights, int heightsSize) {
    int* sorted = (int*)malloc((size_t)heightsSize * sizeof(int));
    memcpy(sorted, heights, (size_t)heightsSize * sizeof(int));
    qsort(sorted, (size_t)heightsSize, sizeof(int), cmpInt);
    int ans = 0;
    for (int i = 0; i < heightsSize; i++) {
        if (heights[i] != sorted[i]) {
            ans++;
        }
    }
    free(sorted);
    return ans;
}
