// LeetCode 1910 - Remove All Occurrences of a Substring
// https://leetcode.com/problems/remove-all-occurrences-of-a-substring/

#include <stdlib.h>
#include <string.h>

char* removeOccurrences(char* s, char* part) {
    int n = (int)strlen(s);
    int m = (int)strlen(part);
    char* stack = (char*)malloc((size_t)n + 1);
    int top = 0;
    for (int i = 0; s[i]; i++) {
        stack[top++] = s[i];
        if (top >= m && memcmp(stack + top - m, part, (size_t)m) == 0) {
            top -= m;
        }
    }
    stack[top] = '\0';
    return stack;
}
