// LeetCode 3707 - Equal Score Substrings
// https://leetcode.com/problems/equal-score-substrings/

#include <stdbool.h>
#include <string.h>

bool scoreBalance(char* s) {
    int l = 0, r = 0;
    int n = (int)strlen(s);
    for (int i = 0; i < n; i++) r += (s[i] - 'a') + 1;
    for (int i = 0; i < n - 1; i++) {
        int x = (s[i] - 'a') + 1;
        l += x; r -= x;
        if (l == r) return true;
    }
    return false;
}
