// LeetCode 0982 - Triples with Bitwise AND Equal To Zero
// https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/

#include <stdlib.h>

int countTriplets(int* nums, int numsSize) {
    int* cnt = (int*)calloc(1 << 16, sizeof(int));
    for (int i = 0; i < numsSize; i++)
        for (int j = 0; j < numsSize; j++)
            cnt[nums[i] & nums[j]]++;
    int ans = 0;
    for (int i = 0; i < numsSize; i++)
        for (int ab = 0; ab < (1 << 16); ab++)
            if ((ab & nums[i]) == 0) ans += cnt[ab];
    free(cnt);
    return ans;
}
