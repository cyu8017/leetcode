// LeetCode 2116 - Check if a Parentheses String Can Be Valid
// https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/

#include <stdbool.h>
#include <string.h>

bool canBeValid(char* s, char* locked) {
    int n = (int)strlen(s);
    if (n % 2 != 0) return false;
    int bal = 0;
    for (int i = 0; i < n; i++) {
        if (locked[i] == '0' || s[i] == '(') bal++;
        else bal--;
        if (bal < 0) return false;
    }
    bal = 0;
    for (int i = n - 1; i >= 0; i--) {
        if (locked[i] == '0' || s[i] == ')') bal++;
        else bal--;
        if (bal < 0) return false;
    }
    return true;
}
