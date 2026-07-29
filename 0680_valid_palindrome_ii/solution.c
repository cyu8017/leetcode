// LeetCode 0680 - Valid Palindrome II
// https://leetcode.com/problems/valid-palindrome-ii/

#include <stdbool.h>
#include <string.h>

static bool isPal(const char* s, int l, int r) {
    while (l < r) {
        if (s[l] != s[r]) return false;
        l++; r--;
    }
    return true;
}

bool validPalindrome(char* s) {
    int l = 0, r = (int)strlen(s) - 1;
    while (l < r) {
        if (s[l] != s[r]) return isPal(s, l + 1, r) || isPal(s, l, r - 1);
        l++; r--;
    }
    return true;
}
