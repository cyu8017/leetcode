// LeetCode 1576 - Replace All ?'s to Avoid Consecutive Repeating Characters
// https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/

#include <stdlib.h>
#include <string.h>

char* modifyString(char* s) {
    int n = (int)strlen(s);
    char* chars = (char*)malloc((size_t)n + 1);
    strcpy(chars, s);
    for (int i = 0; i < n; i++) {
        if (chars[i] == '?') {
            for (char c = 'a'; c <= 'c'; c++) {
                if ((i == 0 || chars[i - 1] != c) && (i + 1 == n || chars[i + 1] != c)) {
                    chars[i] = c;
                    break;
                }
            }
        }
    }
    return chars;
}
