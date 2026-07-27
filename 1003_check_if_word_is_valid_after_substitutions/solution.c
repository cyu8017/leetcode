// LeetCode 1003 - Check If Word Is Valid After Substitutions
// https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

bool isValid(char* s) {
    int n = (int)strlen(s);
    char* stack = (char*)malloc((size_t)n);
    int top = 0;
    for (int i = 0; i < n; i++) {
        stack[top++] = s[i];
        if (top >= 3 && stack[top - 3] == 'a' && stack[top - 2] == 'b' && stack[top - 1] == 'c')
            top -= 3;
    }
    free(stack);
    return top == 0;
}
