// LeetCode 2109 - Adding Spaces to a String
// https://leetcode.com/problems/adding-spaces-to-a-string/

#include <stdlib.h>
#include <string.h>

char* addSpaces(char* s, int* spaces, int spacesSize) {
    int n = (int)strlen(s);
    char* b = (char*)malloc((size_t)n + (size_t)spacesSize + 1);
    int j = 0, bn = 0;
    for (int i = 0; i < n; i++) {
        if (j < spacesSize && spaces[j] == i) { b[bn++] = ' '; j++; }
        b[bn++] = s[i];
    }
    b[bn] = '\0';
    return b;
}
