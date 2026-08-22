// LeetCode 3551 - Minimum Swaps to Sort by Digit Sum
// https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/

#include <stdlib.h>

typedef struct { int ds, v, i; } P3551;

static int digitSum(int x) {
    int s = 0;
    while (x) { s += x % 10; x /= 10; }
    return s;
}

static int cmp_p(const void* a, const void* b) {
    const P3551* x = (const P3551*)a;
    const P3551* y = (const P3551*)b;
    if (x->ds != y->ds) return (x->ds > y->ds) - (x->ds < y->ds);
    return (x->v > y->v) - (x->v < y->v);
}

int minSwaps(int* nums, int numsSize) {
    int n = numsSize;
    P3551* arr = (P3551*)malloc((size_t)n * sizeof(P3551));
    for (int i = 0; i < n; i++) {
        arr[i].ds = digitSum(nums[i]);
        arr[i].v = nums[i];
        arr[i].i = i;
    }
    qsort(arr, (size_t)n, sizeof(P3551), cmp_p);
    /* map value -> target index; values unique in problem */
    int* target = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) {
        /* find where nums[i] should go */
        for (int j = 0; j < n; j++) {
            if (arr[j].v == nums[i]) { target[i] = j; break; }
        }
    }
    char* vis = (char*)calloc((size_t)n, 1);
    int ans = n;
    for (int i = 0; i < n; i++) {
        if (!vis[i]) {
            ans--;
            int j = i;
            while (!vis[j]) {
                vis[j] = 1;
                j = target[j];
            }
        }
    }
    free(arr); free(target); free(vis);
    return ans;
}
