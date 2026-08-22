// LeetCode 2808 - Minimum Seconds to Equalize a Circular Array
// https://leetcode.com/problems/minimum-seconds-to-equalize-a-circular-array/

#include <stdlib.h>

typedef struct { int v, i; } P2808;
static int cmp_p2808(const void* a, const void* b) {
    const P2808* x = a; const P2808* y = b;
    if (x->v != y->v) return (x->v > y->v) - (x->v < y->v);
    return x->i - y->i;
}

int minimumSeconds(int* nums, int numsSize) {
    int n = numsSize;
    P2808* arr = (P2808*)malloc(n * sizeof(P2808));
    for (int i = 0; i < n; i++) { arr[i].v = nums[i]; arr[i].i = i; }
    qsort(arr, n, sizeof(P2808), cmp_p2808);
    int ans = n;
    for (int s = 0; s < n; ) {
        int e = s;
        while (e < n && arr[e].v == arr[s].v) e++;
        int maxGap = 0;
        for (int i = s; i < e; i++) {
            int gap = (i + 1 < e) ? (arr[i + 1].i - arr[i].i) : (arr[s].i + n - arr[i].i);
            if (gap / 2 > maxGap) maxGap = gap / 2;
        }
        if (maxGap < ans) ans = maxGap;
        s = e;
    }
    free(arr);
    return ans;
}
