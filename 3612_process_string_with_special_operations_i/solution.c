// LeetCode 3612 - Process String with Special Operations I
// https://leetcode.com/problems/process-string-with-special-operations-i/

#include <stdlib.h>
#include <string.h>
#include <ctype.h>

char* processStr(char* s) {
    int n = (int)strlen(s);
    char* result = (char*)malloc((size_t)n * n + 1); /* enough for # doubling roughly; grow if needed */
    int cap = n * n + 1, len = 0;
    for (int i = 0; s[i]; i++) {
        char c = s[i];
        if (isalpha((unsigned char)c)) {
            if (len + 1 >= cap) { cap *= 2; result = realloc(result, (size_t)cap); }
            result[len++] = c;
        } else if (c == '*') {
            if (len > 0) len--;
        } else if (c == '#') {
            if (len * 2 + 1 >= cap) { cap = len * 2 + 8; result = realloc(result, (size_t)cap); }
            memcpy(result + len, result, (size_t)len);
            len *= 2;
        } else if (c == '%') {
            for (int l = 0, r = len - 1; l < r; l++, r--) {
                char t = result[l]; result[l] = result[r]; result[r] = t;
            }
        }
    }
    result[len] = '\0';
    return result;
}
