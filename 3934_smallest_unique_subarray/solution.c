// LeetCode 3934 - Smallest Unique Subarray
// https://leetcode.com/problems/smallest-unique-subarray/

#include <stdlib.h>
#include <string.h>

static int* rank3934;
static int* nums3934;
static int n3934, width3934;

static int cmpSA3934(const void* aa, const void* bb) {
    int a = *(const int*)aa, b = *(const int*)bb;
    if (rank3934[a] != rank3934[b]) return rank3934[a] - rank3934[b];
    int ra = (a + width3934 < n3934) ? rank3934[a + width3934] : -1;
    int rb = (b + width3934 < n3934) ? rank3934[b + width3934] : -1;
    return ra - rb;
}

int smallestUniqueSubarray(int* nums, int numsSize) {
    n3934 = numsSize;
    nums3934 = nums;
    int* sa = malloc((size_t)n3934 * sizeof(int));
    rank3934 = malloc((size_t)n3934 * sizeof(int));
    for (int i = 0; i < n3934; i++) { sa[i] = i; rank3934[i] = nums[i]; }
    for (width3934 = 1; width3934 < n3934; width3934 <<= 1) {
        qsort(sa, (size_t)n3934, sizeof(int), cmpSA3934);
        int* next = calloc((size_t)n3934, sizeof(int));
        for (int i = 1; i < n3934; i++) {
            int a = sa[i - 1], b = sa[i];
            int different = rank3934[a] != rank3934[b];
            int ra = (a + width3934 < n3934) ? rank3934[a + width3934] : -1;
            int rb = (b + width3934 < n3934) ? rank3934[b + width3934] : -1;
            next[b] = (different || ra != rb) ? next[a] + 1 : next[a];
        }
        free(rank3934);
        rank3934 = next;
        if (rank3934[sa[n3934 - 1]] == n3934 - 1) break;
    }
    int* pos = malloc((size_t)n3934 * sizeof(int));
    for (int i = 0; i < n3934; i++) pos[sa[i]] = i;
    int* lcp = calloc((size_t)(n3934 > 0 ? n3934 - 1 : 1), sizeof(int));
    int height = 0;
    for (int i = 0; i < n3934; i++) {
        int p = pos[i];
        if (p == n3934 - 1) { height = 0; continue; }
        int j = sa[p + 1];
        while (i + height < n3934 && j + height < n3934 && nums[i + height] == nums[j + height]) height++;
        lcp[p] = height;
        if (height > 0) height--;
    }
    int ans = n3934;
    for (int p = 0; p < n3934; p++) {
        int start = sa[p];
        int need = 1;
        if (p > 0 && lcp[p - 1] + 1 > need) need = lcp[p - 1] + 1;
        if (p + 1 < n3934 && lcp[p] + 1 > need) need = lcp[p] + 1;
        if (need <= n3934 - start && need < ans) ans = need;
    }
    free(sa); free(rank3934); free(pos); free(lcp);
    return ans;
}
