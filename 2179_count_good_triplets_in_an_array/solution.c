// LeetCode 2179 - Count Good Triplets in an Array
// https://leetcode.com/problems/count-good-triplets-in-an-array/

#include <stdlib.h>
#include <string.h>

static void fwAdd(int* bit, int n, int i, int v) {
    for (; i < n; i += i & -i) bit[i] += v;
}
static int fwSum(int* bit, int i) {
    int s = 0;
    for (; i > 0; i -= i & -i) s += bit[i];
    return s;
}

long long goodTriplets(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    (void)nums2Size;
    int n = nums1Size;
    int* pos2 = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) pos2[nums2[i]] = i;
    int* mapped = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) mapped[i] = pos2[nums1[i]];
    int* left = (int*)malloc((size_t)n * sizeof(int));
    int* bit = (int*)calloc((size_t)n + 2, sizeof(int));
    for (int i = 0; i < n; i++) {
        left[i] = fwSum(bit, mapped[i]);
        fwAdd(bit, n + 2, mapped[i] + 1, 1);
    }
    int* right = (int*)malloc((size_t)n * sizeof(int));
    memset(bit, 0, (size_t)(n + 2) * sizeof(int));
    for (int i = n - 1; i >= 0; i--) {
        right[i] = fwSum(bit, n) - fwSum(bit, mapped[i] + 1);
        fwAdd(bit, n + 2, mapped[i] + 1, 1);
    }
    long long ans = 0;
    for (int i = 0; i < n; i++) ans += (long long)left[i] * right[i];
    free(pos2); free(mapped); free(left); free(right); free(bit);
    return ans;
}
