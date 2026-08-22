// LeetCode 2274 - Maximum Consecutive Floors Without Special Floors
// https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors/

#include <stdlib.h>

static int cmp_int(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int maxConsecutive(int bottom, int top, int* special, int specialSize) {
    qsort(special, (size_t)specialSize, sizeof(int), cmp_int);
    int ans = special[0] - bottom;
    for (int i = 1; i < specialSize; i++) {
        int gap = special[i] - special[i - 1] - 1;
        if (gap > ans) ans = gap;
    }
    if (top - special[specialSize - 1] > ans) {
        ans = top - special[specialSize - 1];
    }
    return ans;
}
