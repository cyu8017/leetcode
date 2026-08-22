// LeetCode 2953 - Count Complete Substrings
// https://leetcode.com/problems/count-complete-substrings/

#include <stdlib.h>
#include <string.h>

static int abs_i(int x) { return x < 0 ? -x : x; }

int countCompleteSubstrings(char* word, int k) {
    int n = (int)strlen(word), ans = 0;
    for (int i = 0; i < n; ) {
        int j = i;
        while (j + 1 < n && abs_i((int)word[j + 1] - (int)word[j]) <= 2) j++;
        char* seg = word + i;
        int m = j - i + 1;
        for (int chars = 1; chars <= 26; chars++) {
            int length = chars * k;
            if (length > m) break;
            int freq[26] = {0}, unique = 0;
            for (int r = 0; r < m; r++) {
                int c = seg[r] - 'a';
                freq[c]++;
                if (freq[c] == 1) unique++;
                if (r >= length) {
                    int c2 = seg[r - length] - 'a';
                    freq[c2]--;
                    if (freq[c2] == 0) unique--;
                }
                if (r >= length - 1 && unique == chars) {
                    int ok = 1;
                    for (int t = 0; t < 26; t++) if (freq[t] != 0 && freq[t] != k) { ok = 0; break; }
                    if (ok) ans++;
                }
            }
        }
        i = j + 1;
    }
    return ans;
}
