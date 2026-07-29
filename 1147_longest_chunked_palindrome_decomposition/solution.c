// LeetCode 1147 - Longest Chunked Palindrome Decomposition
// https://leetcode.com/problems/longest-chunked-palindrome-decomposition/

#include <string.h>
#include <stdbool.h>

static bool eqRange(const char* text, int a, int b, int len) {
    for (int i = 0; i < len; i++) if (text[a + i] != text[b + i]) return false;
    return true;
}

int longestDecomposition(char* text) {
    int n = (int)strlen(text);
    int ans = 0, i = 0;
    while (i < n - i) {
        bool found = false;
        int maxLen = (n - 2 * i) / 2;
        for (int length = 1; length <= maxLen; length++) {
            if (eqRange(text, i, n - i - length, length)) {
                ans += 2;
                i += length;
                found = true;
                break;
            }
        }
        if (!found) { ans += 1; break; }
    }
    return ans;
}
