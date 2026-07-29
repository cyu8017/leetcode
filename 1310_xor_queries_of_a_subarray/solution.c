// LeetCode 1310 - XOR Queries of a Subarray
// https://leetcode.com/problems/xor-queries-of-a-subarray/

#include <stdlib.h>

int* xorQueries(int* arr, int arrSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)queriesColSize;
    int* prefix = (int*)malloc((arrSize + 1) * sizeof(int));
    prefix[0] = 0;
    for (int i = 0; i < arrSize; i++) prefix[i + 1] = prefix[i] ^ arr[i];
    int* ans = (int*)malloc(queriesSize * sizeof(int));
    for (int i = 0; i < queriesSize; i++) {
        int left = queries[i][0], right = queries[i][1];
        ans[i] = prefix[right + 1] ^ prefix[left];
    }
    free(prefix);
    *returnSize = queriesSize;
    return ans;
}
