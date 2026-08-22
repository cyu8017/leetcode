// LeetCode 3697 - Compute Decimal Representation
// https://leetcode.com/problems/compute-decimal-representation/

#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* decimalRepresentation(int n, int* returnSize) {
    int tmp[16];
    int tn = 0;
    int p = 1;
    while (n > 0) {
        int v = n % 10;
        n /= 10;
        if (v != 0) tmp[tn++] = p * v;
        p *= 10;
    }
    int* ans = (int*)malloc((size_t)tn * sizeof(int));
    for (int i = 0; i < tn; i++) ans[i] = tmp[tn - 1 - i];
    *returnSize = tn;
    return ans;
}
