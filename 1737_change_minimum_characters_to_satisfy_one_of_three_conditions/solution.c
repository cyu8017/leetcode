// LeetCode 1737 - Change Minimum Characters to Satisfy One of Three Conditions
// https://leetcode.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions/

#include <string.h>

int minCharacters(char* a, char* b) {
    int ca[26] = {0};
    int cb[26] = {0};
    int n = strlen(a);
    int m = strlen(b);
    for (int i = 0; i < n; i++) {
        ca[a[i] - 'a']++;
    }
    for (int i = 0; i < m; i++) {
        cb[b[i] - 'a']++;
    }
    int maxCount = 0;
    for (int i = 0; i < 26; i++) {
        if (ca[i] > maxCount) maxCount = ca[i];
        if (cb[i] > maxCount) maxCount = cb[i];
    }
    int ans = n + m - maxCount;
    int preA = 0, preB = 0;
    for (int code = 0; code < 25; code++) {
        preA += ca[code];
        preB += cb[code];
        int cond1 = n - preA + preB;
        int cond2 = m - preB + preA;
        if (cond1 < ans) ans = cond1;
        if (cond2 < ans) ans = cond2;
    }
    return ans;
}
