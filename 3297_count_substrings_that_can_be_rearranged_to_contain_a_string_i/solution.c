// LeetCode 3297 - Count Substrings That Can Be Rearranged to Contain a String I
// https://leetcode.com/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-i/

#include <string.h>

long long validSubstringCount(char* word1, char* word2) {
    int need[26] = {0}, required = 0;
    for (int i = 0; word2[i]; i++) {
        if (need[word2[i] - 'a'] == 0) required++;
        need[word2[i] - 'a']++;
    }
    int have[26] = {0}, formed = 0, l = 0;
    long long ans = 0;
    int n = (int)strlen(word1);
    for (int r = 0; r < n; r++) {
        int c = word1[r] - 'a';
        have[c]++;
        if (have[c] == need[c] && need[c] > 0) formed++;
        while (formed == required && l <= r) {
            ans += n - r;
            int c2 = word1[l] - 'a';
            if (have[c2] == need[c2] && need[c2] > 0) formed--;
            have[c2]--;
            l++;
        }
    }
    return ans;
}
