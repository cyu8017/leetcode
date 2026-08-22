// LeetCode 3931 - Check Adjacent Digit Differences
// https://leetcode.com/problems/check-adjacent-digit-differences/

#include <stdbool.h>
#include <stdlib.h>

bool isAdjacentDiffAtMostTwo(char* s) {
    for (int i = 1; s[i]; i++) {
        int d = (int)s[i - 1] - (int)s[i];
        if (d < 0) d = -d;
        if (d > 2) return false;
    }
    return true;
}
