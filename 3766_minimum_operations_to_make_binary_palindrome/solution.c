// LeetCode 3766 - Minimum Operations To Make Binary Palindrome
// https://leetcode.com/problems/minimum-operations-to-make-binary-palindrome/

#include <stdlib.h>
#include <limits.h>
#include <string.h>
#include <stdbool.h>

static int* pals;
static int palsN;
static int palsInited = 0;

static bool isPalBin(int i) {
    char s[20];
    int m = 0;
    char rev[20];
    unsigned u = (unsigned)i;
    if (u == 0) { s[0]='0'; m=1; }
    else {
        while (u) { rev[m++] = (char)('0'+(u&1)); u>>=1; }
        for (int j = 0; j < m; j++) s[j] = rev[m-1-j];
    }
    for (int j = 0; j < m/2; j++) if (s[j] != s[m-1-j]) return false;
    return true;
}

static void initPals(void) {
    if (palsInited) return;
    palsInited = 1;
    int N = 1 << 14;
    pals = (int*)malloc((size_t)N * sizeof(int));
    palsN = 0;
    for (int i = 0; i < N; i++) if (isPalBin(i)) pals[palsN++] = i;
}

static int lowerBound(int* a, int n, int x) {
    int lo = 0, hi = n;
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        if (a[mid] < x) lo = mid + 1; else hi = mid;
    }
    return lo;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* minOperations(int* nums, int numsSize, int* returnSize) {
    initPals();
    int* ans = (int*)malloc((size_t)numsSize * sizeof(int));
    for (int k = 0; k < numsSize; k++) {
        int x = nums[k];
        int i = lowerBound(pals, palsN, x);
        int t = INT_MAX;
        if (i < palsN) t = pals[i] - x;
        if (i >= 1) {
            int d = x - pals[i - 1];
            if (d < t) t = d;
        }
        ans[k] = t;
    }
    *returnSize = numsSize;
    return ans;
}
