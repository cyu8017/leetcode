// LeetCode 2967 - Minimum Cost to Make Array Equalindromic
// https://leetcode.com/problems/minimum-cost-to-make-array-equalindromic/

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

static int cmp2967(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

static int makePal2967(int x) {
    char s[32];
    sprintf(s, "%d", x);
    int n = (int)strlen(s);
    for (int i = 0, j = n - 1; i < j; i++, j--) s[j] = s[i];
    return atoi(s);
}

static long long cost2967(int* nums, int n, int p) {
    long long c = 0;
    for (int i = 0; i < n; i++) {
        long long d = (long long)nums[i] - p;
        if (d < 0) d = -d;
        c += d;
    }
    return c;
}

long long minimumCost(int* nums, int numsSize) {
    int* arr = (int*)malloc((size_t)numsSize * sizeof(int));
    for (int i = 0; i < numsSize; i++) arr[i] = nums[i];
    qsort(arr, (size_t)numsSize, sizeof(int), cmp2967);
    int median = arr[numsSize / 2];
    int candidates[32];
    int cn = 0;
    candidates[cn++] = makePal2967(median);
    char s[32];
    sprintf(s, "%d", median);
    int slen = (int)strlen(s);
    char hsbuf[32];
    int halfDigits = (slen + 1) / 2;
    strncpy(hsbuf, s, (size_t)halfDigits);
    hsbuf[halfDigits] = '\0';
    int half = atoi(hsbuf);
    for (int d = -2; d <= 2; d++) {
        int h = half + d;
        if (h <= 0) continue;
        char hs[32];
        sprintf(hs, "%d", h);
        int hlen = (int)strlen(hs);
        char pal[64];
        if (slen % 2 == 0) {
            strcpy(pal, hs);
            for (int i = hlen - 1; i >= 0; i--) {
                int plen = (int)strlen(pal);
                pal[plen] = hs[i];
                pal[plen + 1] = '\0';
            }
        } else {
            strcpy(pal, hs);
            for (int i = hlen - 2; i >= 0; i--) {
                int plen = (int)strlen(pal);
                pal[plen] = hs[i];
                pal[plen + 1] = '\0';
            }
        }
        candidates[cn++] = atoi(pal);
    }
    int extras[] = {1, 9, 11, 99, 101};
    for (int i = 0; i < 5; i++) candidates[cn++] = extras[i];
    long long ans = (1LL << 62);
    for (int i = 0; i < cn; i++) {
        int p = candidates[i];
        if (p <= 0) continue;
        long long c = cost2967(arr, numsSize, p);
        if (c < ans) ans = c;
    }
    free(arr);
    return ans;
}
