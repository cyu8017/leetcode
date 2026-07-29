// LeetCode 0709 - To Lower Case
// https://leetcode.com/problems/to-lower-case/

#include <stdlib.h>
#include <string.h>

char* toLowerCase(char* s) {
    int n = (int)strlen(s);
    char* out = (char*)malloc((size_t)n + 1);
    for (int i = 0; i < n; i++) {
        char ch = s[i];
        if (ch >= 'A' && ch <= 'Z') {
            ch = (char)(ch + 32);
        }
        out[i] = ch;
    }
    out[n] = '\0';
    return out;
}
