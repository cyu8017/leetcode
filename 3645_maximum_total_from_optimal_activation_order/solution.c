// LeetCode 3645 - Maximum Total from Optimal Activation Order
// https://leetcode.com/problems/maximum-total-from-optimal-activation-order/

#include <stdlib.h>
typedef struct { int lim, val; } P;
static int cmp_p(const void* a, const void* b) {
    const P* pa = a; const P* pb = b;
    if (pa->lim != pb->lim) return pa->lim - pb->lim;
    return pb->val - pa->val;
}
long long maxTotal(int* value, int valueSize, int* limit, int limitSize) {
    (void)limitSize;
    P* arr = (P*)malloc((size_t)valueSize * sizeof(P));
    for (int i = 0; i < valueSize; i++) { arr[i].lim = limit[i]; arr[i].val = value[i]; }
    qsort(arr, (size_t)valueSize, sizeof(P), cmp_p);
    long long ans = 0;
    for (int i = 0; i < valueSize; ) {
        int lim = arr[i].lim, j = i;
        while (j < valueSize && arr[j].lim == lim) j++;
        int take = lim < (j - i) ? lim : (j - i);
        for (int t = 0; t < take; t++) ans += arr[i + t].val;
        i = j;
    }
    free(arr);
    return ans;
}
