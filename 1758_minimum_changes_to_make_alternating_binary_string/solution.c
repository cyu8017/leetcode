// LeetCode 1758 - Minimum Changes To Make Alternating Binary String
// https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/

#include <string.h>

int minOperations(char* s) {
    int n = (int)strlen(s);
    int alt1 = 0;
    for (int i = 0; i < n; i++) {
        char expected = (i & 1) == 0 ? '0' : '1';
        if (s[i] != expected) {
            alt1++;
        }
    }
    return alt1 < n - alt1 ? alt1 : n - alt1;
}
