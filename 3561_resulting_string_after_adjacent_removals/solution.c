// LeetCode 3561 - Resulting String After Adjacent Removals
// https://leetcode.com/problems/resulting-string-after-adjacent-removals/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

static int iabs(int x) { return x < 0 ? -x : x; }

static bool isContiguous(char a, char b) {
    int x = iabs((int)a - (int)b);
    return x == 1 || x == 25;
}

char* resultingString(char* s) {
    int n = (int)strlen(s);
    char* stk = (char*)malloc((size_t)n + 1);
    int top = 0;
    for (int i = 0; i < n; i++) {
        char c = s[i];
        if (top > 0 && isContiguous(stk[top - 1], c)) top--;
        else stk[top++] = c;
    }
    stk[top] = '\0';
    return stk;
}
