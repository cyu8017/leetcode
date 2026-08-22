// LeetCode 2831 - Find the Longest Equal Subarray
// https://leetcode.com/problems/find-the-longest-equal-subarray/

#include <stdlib.h>

typedef struct { int v, i; } P;
static int cmp_p(const void* a, const void* b) {
    const P* x = a; const P* y = b;
    if (x->v != y->v) return x->v - y->v;
    return x->i - y->i;
}

int longestEqualSubarray(int* nums, int numsSize, int k) {
    P* arr = (P*)malloc(numsSize * sizeof(P));
    for (int i = 0; i < numsSize; i++) { arr[i].v = nums[i]; arr[i].i = i; }
    qsort(arr, numsSize, sizeof(P), cmp_p);
    int ans = 0;
    for (int s = 0; s < numsSize; ) {
        int e = s;
        while (e < numsSize && arr[e].v == arr[s].v) e++;
        int left = s;
        for (int right = s; right < e; right++) {
            while (arr[right].i - arr[left].i - (right - left) > k) left++;
            if (right - left + 1 > ans) ans = right - left + 1;
        }
        s = e;
    }
    free(arr);
    return ans;
}
