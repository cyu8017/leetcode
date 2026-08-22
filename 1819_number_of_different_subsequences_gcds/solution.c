// LeetCode 1819 - Number of Different Subsequences GCDs
// https://leetcode.com/problems/number-of-different-subsequences-gcds/

#include <stdbool.h>
#include <stdlib.h>

static int gcd(int a, int b) {
    while (b) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}

int countDifferentSubsequenceGCDs(int* nums, int numsSize) {
    int maxVal = nums[0];
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] > maxVal) maxVal = nums[i];
    }
    bool* present = (bool*)calloc((size_t)maxVal + 1, sizeof(bool));
    for (int i = 0; i < numsSize; i++) present[nums[i]] = true;

    int ans = 0;
    for (int g = 1; g <= maxVal; g++) {
        int has = 0;
        int gcdVal = 0;
        for (int multiple = g; multiple <= maxVal; multiple += g) {
            if (present[multiple]) {
                has = 1;
                gcdVal = gcd(gcdVal, multiple / g);
                if (gcdVal == 1) break;
            }
        }
        if (has && gcdVal == 1) ans++;
    }
    free(present);
    return ans;
}
