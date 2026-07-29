// LeetCode 1544 - Make The String Great
// https://leetcode.com/problems/make-the-string-great/

#include <stdlib.h>
#include <string.h>
#include <ctype.h>

char* makeGood(char* s) {
    int n = (int)strlen(s);
    char* stack = (char*)malloc((size_t)n + 1);
    int top = 0;
    for (int i = 0; i < n; i++) {
        if (top > 0 && stack[top - 1] != s[i] && tolower((unsigned char)stack[top - 1]) == tolower((unsigned char)s[i])) {
            top--;
        } else {
            stack[top++] = s[i];
        }
    }
    stack[top] = '\0';
    return stack;
}
