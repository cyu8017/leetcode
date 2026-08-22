// LeetCode 3329 - Count Substrings With K-Frequency Characters II
// https://leetcode.com/problems/count-substrings-with-k-frequency-characters-ii/

#include <string.h>

long long numberOfSubstrings(char* s, int k) {
    int n = (int)strlen(s);
    long long ans = 0;
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
