// LeetCode 1431 - Kids With the Greatest Number of Candies
// https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

#include <stdlib.h>
#include <stdbool.h>

bool* kidsWithCandies(int* candies, int candiesSize, int extraCandies, int* returnSize) {
    int mx = candies[0];
    for (int i = 1; i < candiesSize; i++) if (candies[i] > mx) mx = candies[i];
    bool* ans = (bool*)malloc(candiesSize * sizeof(bool));
    for (int i = 0; i < candiesSize; i++) ans[i] = candies[i] + extraCandies >= mx;
    *returnSize = candiesSize;
    return ans;
}
