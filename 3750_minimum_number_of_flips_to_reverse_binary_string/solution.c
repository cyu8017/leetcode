// LeetCode 3750 - Minimum Number Of Flips To Reverse Binary String
// https://leetcode.com/problems/minimum-number-of-flips-to-reverse-binary-string/

#include <stdio.h>
#include <string.h>

int minimumFlips(int n) {
    char s[64];
    // binary
    unsigned u = (unsigned)n;
    int m = 0;
    char rev[64];
    if (u == 0) { s[0] = '0'; s[1] = 0; m = 1; }
    else {
        while (u) { rev[m++] = (char)('0' + (u & 1)); u >>= 1; }
        for (int i = 0; i < m; i++) s[i] = rev[m - 1 - i];
        s[m] = 0;
    }
    int cnt = 0;
    for (int i = 0; i < m / 2; i++) if (s[i] != s[m - i - 1]) cnt++;
    return cnt * 2;
}
