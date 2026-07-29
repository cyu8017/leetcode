// LeetCode 0796 - Rotate String
// https://leetcode.com/problems/rotate-string/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

bool rotateString(char* s, char* goal) {
    int n = (int)strlen(s);
    if (n != (int)strlen(goal)) return false;
    char* doubled = (char*)malloc((size_t)n * 2 + 1);
    sprintf(doubled, "%s%s", s, s);
    bool ok = strstr(doubled, goal) != NULL;
    free(doubled);
    return ok;
}
