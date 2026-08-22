// LeetCode 2580 - Count Ways to Group Overlapping Ranges
// https://leetcode.com/problems/count-ways-to-group-overlapping-ranges/

#include <stdlib.h>

static int cmpRange(const void* a, const void* b) {
    int* ra = *(int**)a;
    int* rb = *(int**)b;
    return ra[0] - rb[0];
}

int countWays(int** ranges, int rangesSize, int* rangesColSize) {
    (void)rangesColSize;
    const int MOD = 1000000007;
    qsort(ranges, (size_t)rangesSize, sizeof(int*), cmpRange);
    int groups = 0, end = -1;
    for (int i = 0; i < rangesSize; i++) {
        if (ranges[i][0] > end) { groups++; end = ranges[i][1]; }
        else if (ranges[i][1] > end) end = ranges[i][1];
    }
    int ans = 1;
    for (int i = 0; i < groups; i++) ans = ans * 2 % MOD;
    return ans;
}
