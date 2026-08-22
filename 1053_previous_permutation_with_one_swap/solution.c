// LeetCode 1053 - Previous Permutation With One Swap
// https://leetcode.com/problems/previous-permutation-with-one-swap/

#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* prevPermOpt1(int* arr, int arrSize, int* returnSize) {
    int* ans = (int*)malloc((size_t)arrSize * sizeof(int));
    for (int i = 0; i < arrSize; i++) {
        ans[i] = arr[i];
    }
    *returnSize = arrSize;
    int i = arrSize - 2;
    while (i >= 0 && ans[i] <= ans[i + 1]) {
        i--;
    }
    if (i < 0) {
        return ans;
    }
    int j = arrSize - 1;
    while (ans[j] >= ans[i] || ans[j] == ans[j - 1]) {
        j--;
    }
    int tmp = ans[i];
    ans[i] = ans[j];
    ans[j] = tmp;
    return ans;
}
