// LeetCode 1930 - Unique Length-3 Palindromic Subsequences
// https://leetcode.com/problems/unique-length-3-palindromic-subsequences/

#include <string.h>

int countPalindromicSubsequence(char* s) {
    int first[26], last[26];
    for (int i = 0; i < 26; i++) { first[i] = -1; last[i] = -1; }
    int n = (int)strlen(s);
    for (int i = 0; i < n; i++) {
        int c = s[i] - 'a';
        if (first[c] == -1) first[c] = i;
        last[c] = i;
    }
    int ans = 0;
    for (int c = 0; c < 26; c++) {
        if (first[c] == -1 || last[c] - first[c] < 2) continue;
        int seen[26] = {0};
        for (int i = first[c] + 1; i < last[c]; i++) seen[s[i] - 'a'] = 1;
        for (int i = 0; i < 26; i++) ans += seen[i];
    }
    return ans;
}
