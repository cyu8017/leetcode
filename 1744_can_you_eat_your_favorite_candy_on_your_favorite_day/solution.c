// LeetCode 1744 - Can You Eat Your Favorite Candy on Your Favorite Day?
// https://leetcode.com/problems/can-you-eat-your-favorite-candy-on-your-favorite-day/

#include <stdbool.h>
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool* canEat(int* candiesCount, int candiesCountSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    long long* prefix = (long long*)malloc((candiesCountSize + 1) * sizeof(long long));
    prefix[0] = 0;
    for (int i = 0; i < candiesCountSize; i++) {
        prefix[i + 1] = prefix[i] + candiesCount[i];
    }
    bool* ans = (bool*)malloc(queriesSize * sizeof(bool));
    for (int i = 0; i < queriesSize; i++) {
        int candyType = queries[i][0];
        long long day = queries[i][1];
        long long cap = queries[i][2];
        long long minEaten = day + 1;
        long long maxEaten = (day + 1) * cap;
        ans[i] = maxEaten > prefix[candyType] && minEaten <= prefix[candyType + 1];
    }
    free(prefix);
    *returnSize = queriesSize;
    return ans;
}
