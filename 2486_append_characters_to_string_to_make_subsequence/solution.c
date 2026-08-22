// LeetCode 2486 - Append Characters to String to Make Subsequence
// https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

#include <string.h>

int appendCharacters(char* s, char* t) {
    int j = 0, nt = (int)strlen(t), ns = (int)strlen(s);
    for (int i = 0; i < ns && j < nt; i++) {
        if (s[i] == t[j]) j++;
    }
    return nt - j;
}
