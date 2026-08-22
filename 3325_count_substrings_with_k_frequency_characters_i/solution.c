// LeetCode 3325 - Count Substrings With K-Frequency Characters I
// https://leetcode.com/problems/count-substrings-with-k-frequency-characters-i/

#include <string.h>

int numberOfSubstrings(char* s, int k) {
    int n = (int)strlen(s), ans = 0;
    for (int i = 0; i < n; i++) {
        int freq[26] = {0};
        for (int j = i; j < n; j++) {
            freq[s[j] - 'a']++;
            int ok = 0;
            for (int t = 0; t < 26; t++) if (freq[t] >= k) { ok = 1; break; }
            if (ok) { ans += n - j; break; }
        }
    }
    return ans;
}
