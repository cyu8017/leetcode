// LeetCode 2519 - Count the Number of K-Big Indices
// https://leetcode.com/problems/count-the-number-of-k-big-indices/

#include <stdlib.h>
#include <string.h>

static void ft_add(int* bit, int n, int i, int v) {
    for (; i <= n; i += i & -i) bit[i] += v;
}
static int ft_sum(int* bit, int i) {
    int s = 0;
    for (; i > 0; i -= i & -i) s += bit[i];
    return s;
}

static int cmp_int(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int kBigIndices(int* nums, int numsSize, int k) {
    int n = numsSize;
    int* uniq = (int*)malloc((size_t)n * sizeof(int));
    memcpy(uniq, nums, (size_t)n * sizeof(int));
    qsort(uniq, (size_t)n, sizeof(int), cmp_int);
    int w = 0;
    for (int i = 0; i < n; i++) if (i == 0 || uniq[i] != uniq[i - 1]) uniq[w++] = uniq[i];
    int* rank = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) {
        int lo = 0, hi = w - 1, ans = 0;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (uniq[mid] == nums[i]) { ans = mid + 1; break; }
            if (uniq[mid] < nums[i]) lo = mid + 1;
            else hi = mid - 1;
        }
        rank[i] = ans;
    }
    int m = w;
    int* left = (int*)malloc((size_t)n * sizeof(int));
    int* bit = (int*)calloc((size_t)(m + 2), sizeof(int));
    for (int i = 0; i < n; i++) {
        left[i] = ft_sum(bit, rank[i] - 1);
        ft_add(bit, m, rank[i], 1);
    }
    memset(bit, 0, (size_t)(m + 2) * sizeof(int));
    int* right = (int*)malloc((size_t)n * sizeof(int));
    for (int i = n - 1; i >= 0; i--) {
        right[i] = ft_sum(bit, rank[i] - 1);
        ft_add(bit, m, rank[i], 1);
    }
    int ans = 0;
    for (int i = 0; i < n; i++) if (left[i] >= k && right[i] >= k) ans++;
    free(uniq); free(rank); free(left); free(right); free(bit);
    return ans;
}
