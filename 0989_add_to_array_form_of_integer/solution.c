// LeetCode 0989 - Add to Array-Form of Integer
// https://leetcode.com/problems/add-to-array-form-of-integer/

#include <stdlib.h>

int* addToArrayForm(int* num, int numSize, int k, int* returnSize) {
    int cap = numSize + 10;
    int* ans = (int*)malloc((size_t)cap * sizeof(int));
    int n = 0;
    int i = numSize - 1;
    while (i >= 0 || k) {
        if (i >= 0) k += num[i--];
        ans[n++] = k % 10;
        k /= 10;
    }
    for (int L = 0, R = n - 1; L < R; L++, R--) { int t = ans[L]; ans[L] = ans[R]; ans[R] = t; }
    *returnSize = n;
    return ans;
}
