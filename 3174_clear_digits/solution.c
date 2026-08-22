// LeetCode 3174 - Clear Digits
// https://leetcode.com/problems/clear-digits/

#include <stdlib.h>
#include <string.h>

char* clearDigits(char* s) {
    int n = (int)strlen(s);
    char* stk = malloc(n + 1);
    int top = 0;
    for (int i = 0; i < n; i++) {
        if (s[i] >= '0' && s[i] <= '9') { if (top > 0) top--; }
        else stk[top++] = s[i];
    }
    stk[top] = 0;
    return stk;
}
