// LeetCode 2367 - Number of Arithmetic Triplets
// https://leetcode.com/problems/number-of-arithmetic-triplets/

#include <stdbool.h>

int arithmeticTriplets(int* nums, int numsSize, int diff) {
    bool seen[201] = {0};
    for (int i = 0; i < numsSize; i++) seen[nums[i]] = true;
    int ans = 0;
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i];
        if (x + diff <= 200 && x + 2 * diff <= 200 && seen[x + diff] && seen[x + 2 * diff]) ans++;
    }
    return ans;
}
