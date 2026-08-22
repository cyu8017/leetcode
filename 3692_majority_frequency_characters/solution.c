// LeetCode 3692 - Majority Frequency Characters
// https://leetcode.com/problems/majority-frequency-characters/

#include <stdlib.h>
#include <string.h>

char* majorityFrequencyGroup(char* s) {
    int cnt[26] = {0};
    for (int i = 0; s[i]; i++) cnt[s[i] - 'a']++;
    char groups[101][27];
    int glen[101] = {0};
    memset(groups, 0, sizeof(groups));
    for (int i = 0; i < 26; i++) {
        int v = cnt[i];
        if (v > 0) groups[v][glen[v]++] = (char)('a' + i);
    }
    int mx = 0, mv = 0;
    for (int v = 1; v <= 100; v++) {
        if (glen[v] > mx || (glen[v] == mx && v > mv)) {
            mx = glen[v];
            mv = v;
        }
    }
    char* ans = (char*)malloc((size_t)(mx + 1));
    memcpy(ans, groups[mv], (size_t)mx);
    ans[mx] = 0;
    return ans;
}
