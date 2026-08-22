// LeetCode 3389 - Minimum Operations to Make Character Frequencies Equal
// https://leetcode.com/problems/minimum-operations-to-make-character-frequencies-equal/

#include <string.h>

int makeStringGood(char* s) {
    int freq[26] = {0}, n = (int)strlen(s);
    for (int i = 0; i < n; i++) freq[s[i] - 'a']++;
    int ans = n;
    for (int t = 1; t <= n; t++) {
        int pool = 0, deficit = 0;
        for (int i = 0; i < 26; i++) {
            if (freq[i] > t) pool += freq[i] - t;
            else if (freq[i] < t && freq[i] > 0) deficit += t - freq[i];
            else if (freq[i] == 0) deficit += t; /* letters with 0 also need to reach t? Go only iterates existing freq array which includes 0s */
        }
        /* Go iterates all 26 including zeros */
        pool = 0; deficit = 0;
        for (int i = 0; i < 26; i++) {
            if (freq[i] > t) pool += freq[i] - t;
            if (freq[i] < t) deficit += t - freq[i];
        }
        int ops = pool >= deficit ? pool : deficit;
        if (ops < ans) ans = ops;
    }
    if (n < ans) ans = n;
    return ans;
}
