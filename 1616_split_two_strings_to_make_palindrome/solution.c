// LeetCode 1616 - Split Two Strings to Make Palindrome
// https://leetcode.com/problems/split-two-strings-to-make-palindrome/

#include <stdbool.h>
#include <string.h>

static bool isPal(const char* s, int i, int j) {
    while (i < j) {
        if (s[i] != s[j]) return false;
        i++; j--;
    }
    return true;
}

static bool check(const char* x, const char* y) {
    int i = 0, j = (int)strlen(x) - 1;
    while (i < j && x[i] == y[j]) { i++; j--; }
    return isPal(x, i, j) || isPal(y, i, j);
}

bool checkPalindromeFormation(char* a, char* b) {
    return check(a, b) || check(b, a);
}
