// LeetCode 1864 - Minimum Number of Swaps to Make the Binary String Alternating
// https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/

#include <stdlib.h>
#include <string.h>

static int mismatches(const char* s, int n, char first) {
    int bad = 0;
    for (int i = 0; i < n; i++) {
        char expect = (i % 2 == 0) ? first : (char)('0' + '1' - first);
        if (s[i] != expect) bad++;
    }
    return bad / 2;
}

int minSwaps(char* s) {
    int n = (int)strlen(s);
    int zeros = 0;
    for (int i = 0; i < n; i++) if (s[i] == '0') zeros++;
    int ones = n - zeros;
    int diff = zeros - ones;
    if (diff < 0) diff = -diff;
    if (diff > 1) return -1;
    if (zeros == ones) {
        int a = mismatches(s, n, '0');
        int b = mismatches(s, n, '1');
        return a < b ? a : b;
    }
    if (zeros > ones) return mismatches(s, n, '0');
    return mismatches(s, n, '1');
}
