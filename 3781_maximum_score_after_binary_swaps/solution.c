// LeetCode 3781 - Maximum Score After Binary Swaps
// https://leetcode.com/problems/maximum-score-after-binary-swaps/

#include <stdlib.h>
#include <string.h>

static void push3781(int* h, int* n, int x) {
    int i = (*n)++;
    h[i] = x;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h[p] >= h[i]) break;
        int t = h[p]; h[p] = h[i]; h[i] = t;
        i = p;
    }
}
static int pop3781(int* h, int* n) {
    int r = h[0];
    h[0] = h[--(*n)];
    int i = 0;
    for (;;) {
        int l = 2 * i + 1, rgt = 2 * i + 2, s = i;
        if (l < *n && h[l] > h[s]) s = l;
        if (rgt < *n && h[rgt] > h[s]) s = rgt;
        if (s == i) break;
        int t = h[i]; h[i] = h[s]; h[s] = t;
        i = s;
    }
    return r;
}

long long maximumScore(int* nums, int numsSize, char* s) {
    long long ans = 0;
    int* pq = (int*)malloc((size_t)numsSize * sizeof(int));
    int psz = 0;
    int n = (int)strlen(s);
    if (n > numsSize) n = numsSize;
    for (int i = 0; i < n; i++) {
        push3781(pq, &psz, nums[i]);
        if (s[i] == '1' && psz > 0) ans += pop3781(pq, &psz);
    }
    free(pq);
    return ans;
}
