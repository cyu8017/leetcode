// LeetCode 2182 - Construct String With Repeat Limit
// https://leetcode.com/problems/construct-string-with-repeat-limit/

#include <stdlib.h>
#include <string.h>

char* repeatLimitedString(char* s, int repeatLimit) {
    int freq[26] = {0};
    int n = (int)strlen(s);
    for (int i = 0; i < n; i++) freq[s[i] - 'a']++;
    char* ans = (char*)malloc((size_t)n + 1);
    int an = 0;
    for (;;) {
        int placed = 0;
        for (int c = 25; c >= 0; c--) {
            if (freq[c] == 0) continue;
            if (an > 0 && ans[an - 1] - 'a' == c) {
                int found = 0;
                for (int d = c - 1; d >= 0; d--) {
                    if (freq[d] > 0) {
                        ans[an++] = (char)('a' + d);
                        freq[d]--;
                        found = 1; placed = 1;
                        break;
                    }
                }
                if (!found) { ans[an] = '\0'; return ans; }
                break;
            }
            int use = freq[c] < repeatLimit ? freq[c] : repeatLimit;
            for (int i = 0; i < use; i++) ans[an++] = (char)('a' + c);
            freq[c] -= use;
            placed = 1;
            break;
        }
        if (!placed) break;
    }
    ans[an] = '\0';
    return ans;
}
