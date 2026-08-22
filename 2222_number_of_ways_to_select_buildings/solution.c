// LeetCode 2222 - Number of Ways to Select Buildings
// https://leetcode.com/problems/number-of-ways-to-select-buildings/

#include <string.h>

long long numberOfWays(char* s) {
    int n = (int)strlen(s);
    int total0 = 0, total1 = 0;
    for (int i = 0; i < n; i++) {
        if (s[i] == '0') total0++;
        else total1++;
    }
    int left0 = 0, left1 = 0;
    long long ans = 0;
    for (int i = 0; i < n; i++) {
        if (s[i] == '0') {
            ans += (long long)left1 * (total1 - left1);
            left0++;
        } else {
            ans += (long long)left0 * (total0 - left0);
            left1++;
        }
    }
    return ans;
}
