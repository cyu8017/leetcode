// LeetCode 3335 - Total Characters in String After Transformations I
// https://leetcode.com/problems/total-characters-in-string-after-transformations-i/

#include <string.h>

int lengthAfterTransformations(char* s, int t) {
    const int mod = 1000000007;
    int cnt[26] = {0};
    for (int i = 0; s[i]; i++) cnt[s[i] - 'a']++;
    for (int step = 0; step < t; step++) {
        int ncnt[26] = {0};
        for (int i = 0; i < 25; i++) ncnt[i + 1] = (ncnt[i + 1] + cnt[i]) % mod;
        ncnt[0] = (ncnt[0] + cnt[25]) % mod;
        ncnt[1] = (ncnt[1] + cnt[25]) % mod;
        memcpy(cnt, ncnt, sizeof(cnt));
    }
    int ans = 0;
    for (int i = 0; i < 26; i++) ans = (ans + cnt[i]) % mod;
    return ans;
}
