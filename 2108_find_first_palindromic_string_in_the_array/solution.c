// LeetCode 2108 - Find First Palindromic String in the Array
// https://leetcode.com/problems/find-first-palindromic-string-in-the-array/

#include <string.h>
#include <stdbool.h>

char* firstPalindrome(char** words, int wordsSize) {
    for (int i = 0; i < wordsSize; i++) {
        char* w = words[i];
        int l = 0, r = (int)strlen(w) - 1;
        bool ok = true;
        while (l < r) {
            if (w[l] != w[r]) { ok = false; break; }
            l++; r--;
        }
        if (ok) return w;
    }
    return "";
}
