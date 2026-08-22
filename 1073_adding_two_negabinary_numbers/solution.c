// LeetCode 1073 - Adding Two Negabinary Numbers
// https://leetcode.com/problems/adding-two-negabinary-numbers/

#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* addNegabinary(int* arr1, int arr1Size, int* arr2, int arr2Size, int* returnSize) {
    int cap = arr1Size + arr2Size + 4;
    int* tmp = (int*)malloc((size_t)cap * sizeof(int));
    int len = 0;
    int i = arr1Size - 1, j = arr2Size - 1, carry = 0;
    while (i >= 0 || j >= 0 || carry) {
        int total = carry;
        if (i >= 0) {
            total += arr1[i--];
        }
        if (j >= 0) {
            total += arr2[j--];
        }
        tmp[len++] = total & 1;
        carry = -(total >> 1);
    }
    while (len > 1 && tmp[len - 1] == 0) {
        len--;
    }
    int* ans = (int*)malloc((size_t)len * sizeof(int));
    for (int k = 0; k < len; k++) {
        ans[k] = tmp[len - 1 - k];
    }
    free(tmp);
    *returnSize = len;
    return ans;
}
