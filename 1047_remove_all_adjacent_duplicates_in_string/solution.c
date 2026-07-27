// LeetCode 1047 - Remove All Adjacent Duplicates In String
// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

#include <stdlib.h>
#include <string.h>

char* removeDuplicates(char* s) {
    int n = (int)strlen(s);
    char* stack = (char*)malloc((size_t)n + 1);
    int top = 0;
    for (int i = 0; i < n; i++) {
        if (top > 0 && stack[top - 1] == s[i]) top--;
        else stack[top++] = s[i];
    }
    stack[top] = '\0';
    return stack;
}
