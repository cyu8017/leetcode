// LeetCode 0647 - Palindromic Substrings
// https://leetcode.com/problems/palindromic-substrings/

#include <string.h>

static int expand(const char* s, int left, int right, int n) {
    int count = 0;
    while (left >= 0 && right < n && s[left] == s[right]) {
        count++;
        left--;
        right++;
    }
    return count;
}

int countSubstrings(char* s) {
    int n = (int)strlen(s);
    int total = 0;
    for (int i = 0; i < n; i++) {
        total += expand(s, i, i, n);
        total += expand(s, i, i + 1, n);
    }
    return total;
}
