// LeetCode 3448 - Count Substrings Divisible By Last Digit
// https://leetcode.com/problems/count-substrings-divisible-by-last-digit/

#include <string.h>

long long countSubstrings(char* s) {
    long long ans = 0;
    int n = (int)strlen(s);
    for (int r = 0; r < n; r++) {
        int last = s[r] - '0';
        if (last == 0) continue;
        int mod = 0, p = 1 % last;
        for (int l = r; l >= 0; l--) {
            mod = (mod + (s[l] - '0') * p) % last;
            p = (p * 10) % last;
            if (mod == 0) ans++;
        }
    }
    return ans;
}
