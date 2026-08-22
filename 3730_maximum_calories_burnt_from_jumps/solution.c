// LeetCode 3730 - Maximum Calories Burnt from Jumps
// https://leetcode.com/problems/maximum-calories-burnt-from-jumps/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

long long maxCaloriesBurnt(int* heights, int heightsSize) {
    qsort(heights, (size_t)heightsSize, sizeof(int), cmpInt);
    long long ans = 0;
    int pre = 0;
    int l = 0, r = heightsSize - 1;
    while (l < r) {
        long long d1 = heights[r] - pre;
        ans += d1 * d1;
        long long d2 = heights[l] - heights[r];
        ans += d2 * d2;
        pre = heights[l];
        l++; r--;
    }
    long long d = heights[r] - pre;
    ans += d * d;
    return ans;
}
