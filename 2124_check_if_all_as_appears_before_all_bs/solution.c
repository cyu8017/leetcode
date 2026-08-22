// LeetCode 2124 - Check if All A's Appears Before All B's
// https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/

#include <stdbool.h>

bool checkString(char* s) {
    int seenB = 0;
    for (int i = 0; s[i]; i++) {
        if (s[i] == 'b') seenB = 1;
        else if (seenB) return false;
    }
    return true;
}
