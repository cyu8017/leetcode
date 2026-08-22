// LeetCode 2696 - Minimum String Length After Removing Substrings
// https://leetcode.com/problems/minimum-string-length-after-removing-substrings/

#include <stdlib.h>
#include <string.h>

int minLength(char* s) {
    int n = (int)strlen(s);
    char* stack = (char*)malloc((size_t)n + 1);
    int top = 0;
    for (int i = 0; i < n; i++) {
        char c = s[i];
        if (top > 0) {
            char t = stack[top - 1];
            if ((t == 'A' && c == 'B') || (t == 'C' && c == 'D')) {
                top--;
                continue;
            }
        }
        stack[top++] = c;
    }
    free(stack);
    return top;
}
