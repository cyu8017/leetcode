// LeetCode 2263 - Make Array Non-decreasing or Non-increasing
// https://leetcode.com/problems/make-array-non-decreasing-or-non-increasing/

#include <stdlib.h>

static void heap_swap(int* a, int i, int j) { int t = a[i]; a[i] = a[j]; a[j] = t; }
static void heap_up_max(int* a, int i) {
    while (i > 0) {
        int p = (i - 1) / 2;
        if (a[p] >= a[i]) break;
        heap_swap(a, p, i); i = p;
    }
}
static void heap_down_max(int* a, int n, int i) {
    for (;;) {
        int l = 2 * i + 1, r = l + 1, s = i;
        if (l < n && a[l] > a[s]) s = l;
        if (r < n && a[r] > a[s]) s = r;
        if (s == i) break;
        heap_swap(a, i, s); i = s;
    }
}

static int cost_arr(int* arr, int n) {
    int* h = (int*)malloc((size_t)n * sizeof(int));
    int hn = 0, ans = 0;
    for (int i = 0; i < n; i++) {
        int x = arr[i];
        if (hn > 0 && h[0] > x) {
            ans += h[0] - x;
            h[0] = h[--hn];
            if (hn > 0) heap_down_max(h, hn, 0);
            h[hn++] = x;
            heap_up_max(h, hn - 1);
        }
        h[hn++] = x;
        heap_up_max(h, hn - 1);
    }
    free(h);
    return ans;
}

int convertArray(int* nums, int numsSize) {
    int* rev = (int*)malloc((size_t)numsSize * sizeof(int));
    for (int i = 0; i < numsSize; i++) rev[numsSize - 1 - i] = nums[i];
    int a = cost_arr(nums, numsSize);
    int b = cost_arr(rev, numsSize);
    free(rev);
    return a < b ? a : b;
}
