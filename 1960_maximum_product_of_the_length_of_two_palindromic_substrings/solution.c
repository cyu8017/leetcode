// LeetCode 1960 - Maximum Product of the Length of Two Palindromic Substrings
// https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-substrings/

#include <stdlib.h>
#include <string.h>

long long maxProduct(char* s) {
    int n = (int)strlen(s);
    int* radius = (int*)calloc((size_t)n, sizeof(int));
    int center = 0, right = 0;
    for (int i = 0; i < n; i++) {
        if (i < right) {
            int mir = 2 * center - i;
            int v = right - i;
            radius[i] = v < radius[mir] ? v : radius[mir];
        }
        while (i - radius[i] - 1 >= 0 && i + radius[i] + 1 < n &&
               s[i - radius[i] - 1] == s[i + radius[i] + 1]) {
            radius[i]++;
        }
        if (i + radius[i] > right) {
            center = i;
            right = i + radius[i];
        }
    }
    int* end = (int*)malloc((size_t)n * sizeof(int));
    int* start = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) { end[i] = 1; start[i] = 1; }
    for (int i = 0; i < n; i++) {
        int r = radius[i];
        if (2 * r + 1 > end[i + r]) end[i + r] = 2 * r + 1;
        if (2 * r + 1 > start[i - r]) start[i - r] = 2 * r + 1;
    }
    for (int i = n - 2; i >= 0; i--) {
        int v = end[i + 1] - 2;
        if (v > end[i]) end[i] = v;
    }
    for (int i = 1; i < n; i++) {
        int v = start[i - 1] - 2;
        if (v > start[i]) start[i] = v;
    }
    int* pre = (int*)malloc((size_t)n * sizeof(int));
    int* suf = (int*)malloc((size_t)n * sizeof(int));
    pre[0] = end[0];
    for (int i = 1; i < n; i++) pre[i] = pre[i - 1] > end[i] ? pre[i - 1] : end[i];
    suf[n - 1] = start[n - 1];
    for (int i = n - 2; i >= 0; i--) suf[i] = suf[i + 1] > start[i] ? suf[i + 1] : start[i];
    long long ans = 0;
    for (int i = 0; i < n - 1; i++) {
        long long prod = (long long)pre[i] * suf[i + 1];
        if (prod > ans) ans = prod;
    }
    free(radius); free(end); free(start); free(pre); free(suf);
    return ans;
}
