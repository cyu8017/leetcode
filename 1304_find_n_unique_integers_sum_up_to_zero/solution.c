// LeetCode 1304 - Find N Unique Integers Sum Up to Zero
// https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

#include <stdlib.h>

int* sumZero(int n, int* returnSize) {
    int* ans = (int*)malloc(n * sizeof(int));
    int idx = 0;
    for (int v = 1; v <= n / 2; v++) {
        ans[idx++] = -v;
        ans[idx++] = v;
    }
    if (n % 2) ans[idx++] = 0;
    *returnSize = n;
    return ans;
}
