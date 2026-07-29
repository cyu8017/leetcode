// LeetCode 1940 - Longest Common Subsequence Between Sorted Arrays
// https://leetcode.com/problems/longest-common-subsequence-between-sorted-arrays/

#include <stdlib.h>

int* longestCommonSubsequence(int** arrays, int arraysSize, int* arraysColSize, int* returnSize) {
    int cnt[101] = {0};
    for (int i = 0; i < arraysSize; i++) {
        for (int j = 0; j < arraysColSize[i]; j++) cnt[arrays[i][j]]++;
    }
    int* res = (int*)malloc(100 * sizeof(int));
    int sz = 0;
    for (int j = 0; j < arraysColSize[0]; j++) {
        int x = arrays[0][j];
        if (cnt[x] == arraysSize) res[sz++] = x;
    }
    *returnSize = sz;
    return res;
}
