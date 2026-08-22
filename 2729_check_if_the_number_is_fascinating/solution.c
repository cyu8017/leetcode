// LeetCode 2729 - Check if The Number is Fascinating
// https://leetcode.com/problems/check-if-the-number-is-fascinating/

#include <stdio.h>
#include <stdbool.h>
#include <string.h>

bool isFascinating(int n) {
    char s[32];
    sprintf(s, "%d%d%d", n, 2 * n, 3 * n);
    if ((int)strlen(s) != 9) return false;
    bool seen[10] = {0};
    for (int i = 0; s[i]; i++) {
        int d = s[i] - '0';
        if (d == 0 || seen[d]) return false;
        seen[d] = true;
    }
    return true;
}
