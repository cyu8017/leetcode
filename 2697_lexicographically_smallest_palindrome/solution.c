// LeetCode 2697 - Lexicographically Smallest Palindrome
// https://leetcode.com/problems/lexicographically-smallest-palindrome/

#include <stdlib.h>
#include <string.h>

char* makeSmallestPalindrome(char* s) {
    int n = (int)strlen(s);
    char* b = (char*)malloc((size_t)n + 1);
    memcpy(b, s, (size_t)n + 1);
    int l = 0, r = n - 1;
    while (l < r) {
        if (b[l] != b[r]) {
            if (b[l] < b[r]) b[r] = b[l];
            else b[l] = b[r];
        }
        l++; r--;
    }
    return b;
}
