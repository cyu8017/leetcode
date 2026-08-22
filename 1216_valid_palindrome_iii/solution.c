// LeetCode 1216 - Valid Palindrome III
// https://leetcode.com/problems/valid-palindrome-iii/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

bool isValidPalindrome(char* s, int k) {
    int n = (int)strlen(s);
    if (n == 0) return true;
    int* dp = (int*)calloc((size_t)n, sizeof(int));
    for (int i = n - 1; i >= 0; i--) {
        int previous = 0;
        for (int j = i + 1; j < n; j++) {
            int old = dp[j];
            if (s[i] == s[j]) dp[j] = previous;
            else {
                int a = dp[j];
                int b = dp[j - 1];
                dp[j] = 1 + (a < b ? a : b);
            }
            previous = old;
        }
    }
    bool ans = dp[n - 1] <= k;
    free(dp);
    return ans;
}
