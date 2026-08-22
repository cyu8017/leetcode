// LeetCode 2575 - Find the Divisibility Array of a String
// https://leetcode.com/problems/find-the-divisibility-array-of-a-string/

#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* divisibilityArray(char* word, int m, int* returnSize) {
    int n = (int)strlen(word);
    int* ans = (int*)calloc((size_t)n, sizeof(int));
    long long cur = 0;
    for (int i = 0; i < n; i++) {
        cur = (cur * 10 + (word[i] - '0')) % m;
        if (cur == 0) ans[i] = 1;
    }
    *returnSize = n;
    return ans;
}
