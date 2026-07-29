// LeetCode 1312 - Minimum Insertion Steps to Make a String Palindrome
// https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/

#include <stdlib.h>
#include <string.h>

int minInsertions(char* s) {
    int n = (int)strlen(s);
    if (n == 0) return 0;
    int* dp = (int*)calloc(n, sizeof(int));
    for (int left = n - 2; left >= 0; left--) {
        int diagonal = 0;
        for (int right = left + 1; right < n; right++) {
            int old = dp[right];
            if (s[left] == s[right]) dp[right] = diagonal;
            else {
                int a = dp[right], b = dp[right - 1];
                dp[right] = 1 + (a < b ? a : b);
            }
            diagonal = old;
        }
    }
    int ans = dp[n - 1];
    free(dp);
    return ans;
}
