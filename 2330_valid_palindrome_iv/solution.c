// LeetCode 2330 - Valid Palindrome IV
// https://leetcode.com/problems/valid-palindrome-iv/

#include <stdbool.h>
#include <string.h>

bool makePalindrome(char* s) {
    int n = (int)strlen(s);
    int diff = 0;
    for (int i = 0, j = n - 1; i < j; i++, j--) {
        if (s[i] != s[j]) {
            diff++;
            if (diff > 2) return false;
        }
    }
    return true;
}
