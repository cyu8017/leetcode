// LeetCode 2426 - Number of Pairs Satisfying Inequality
// https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

#include <stdlib.h>

static int* g_arr;
static int* g_tmp;
static int g_diff;

static long long mergeCount(int l, int r) {
    if (r - l <= 1) return 0;
    int m = (l + r) / 2;
    long long ans = mergeCount(l, m) + mergeCount(m, r);
    int j = m;
    for (int i = l; i < m; i++) {
        while (j < r && g_arr[j] < g_arr[i] - g_diff) j++;
        ans += r - j;
    }
    int i = l, p = l, q = m;
    while (p < m && q < r) {
        if (g_arr[p] <= g_arr[q]) g_tmp[i++] = g_arr[p++];
        else g_tmp[i++] = g_arr[q++];
    }
    while (p < m) g_tmp[i++] = g_arr[p++];
    while (q < r) g_tmp[i++] = g_arr[q++];
    for (int k = l; k < r; k++) g_arr[k] = g_tmp[k];
    return ans;
}

long long numberOfPairs(int* nums1, int nums1Size, int* nums2, int nums2Size, int diff) {
    (void)nums2Size;
    int n = nums1Size;
    g_arr = (int*)malloc((size_t)n * sizeof(int));
    g_tmp = (int*)malloc((size_t)n * sizeof(int));
    g_diff = diff;
    for (int i = 0; i < n; i++) g_arr[i] = nums1[i] - nums2[i];
    long long ans = mergeCount(0, n);
    free(g_arr); free(g_tmp);
    return ans;
}
