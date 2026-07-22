// LeetCode 1646 - Get Maximum in Generated Array
// https://leetcode.com/problems/get-maximum-in-generated-array/

#include <stdlib.h>

int getMaximumGenerated(int n) {
    if (n < 2) return n;
    int* a = (int*)malloc((size_t)(n + 1) * sizeof(int));
    a[0] = 0; a[1] = 1;
    int best = 1;
    for (int i = 2; i <= n; i++) {
        a[i] = (i % 2 == 0) ? a[i / 2] : a[i / 2] + a[i / 2 + 1];
        if (a[i] > best) best = a[i];
    }
    free(a);
    return best;
}
