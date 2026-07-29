// LeetCode 0678 - Valid Parenthesis String
// https://leetcode.com/problems/valid-parenthesis-string/

#include <stdbool.h>

bool checkValidString(char* s) {
    int low = 0, high = 0;
    for (char* p = s; *p; p++) {
        if (*p == '(') { low++; high++; }
        else if (*p == ')') { low--; high--; }
        else { low--; high++; }
        if (high < 0) return false;
        if (low < 0) low = 0;
    }
    return low == 0;
}
