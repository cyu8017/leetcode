// LeetCode 0844 - Backspace String Compare
// https://leetcode.com/problems/backspace-string-compare/

#include <stdbool.h>
#include <string.h>

static void build(const char* s, char* stack) {
    int top = 0;
    for (int i = 0; s[i]; i++) {
        if (s[i] == '#') { if (top > 0) top--; }
        else stack[top++] = s[i];
    }
    stack[top] = '\0';
}

bool backspaceCompare(char* s, char* t) {
    char a[201], b[201];
    build(s, a);
    build(t, b);
    return strcmp(a, b) == 0;
}
