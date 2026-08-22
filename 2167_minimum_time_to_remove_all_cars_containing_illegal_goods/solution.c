// LeetCode 2167 - Minimum Time to Remove All Cars Containing Illegal Goods
// https://leetcode.com/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/

#include <stdlib.h>
#include <string.h>

int minimumTime(char* s) {
    int n = (int)strlen(s);
    int* left = (int*)calloc((size_t)n, sizeof(int));
    if (s[0] == '1') left[0] = 1;
    for (int i = 1; i < n; i++) {
        left[i] = left[i - 1];
        if (s[i] == '1') {
            int cand = left[i - 1] + 2;
            left[i] = (i + 1 < cand) ? i + 1 : cand;
        }
    }
    int ans = left[n - 1], right = 0;
    for (int i = n - 1; i >= 0; i--) {
        if (s[i] == '1') {
            int cand = right + 2;
            right = (n - i < cand) ? n - i : cand;
        }
        int leftCost = i > 0 ? left[i - 1] : 0;
        if (leftCost + right < ans) ans = leftCost + right;
    }
    free(left);
    return ans;
}
