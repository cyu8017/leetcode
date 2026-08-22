// LeetCode 3571 - Find the Shortest Superstring II
// https://leetcode.com/problems/find-the-shortest-superstring-ii/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

static bool contains(const char* hay, const char* needle) {
    return strstr(hay, needle) != NULL;
}

char* shortestSuperstring(char* s1, char* s2) {
    int m = (int)strlen(s1), n = (int)strlen(s2);
    if (m > n) return shortestSuperstring(s2, s1);
    if (contains(s2, s1)) {
        char* r = (char*)malloc((size_t)n + 1);
        strcpy(r, s2);
        return r;
    }
    for (int i = 0; i < m; i++) {
        if (strncmp(s2, s1 + i, (size_t)(m - i)) == 0) {
            char* r = (char*)malloc((size_t)i + n + 1);
            memcpy(r, s1, (size_t)i);
            strcpy(r + i, s2);
            return r;
        }
        if (n >= m - i && strncmp(s2 + n - (m - i), s1, (size_t)(m - i)) == 0) {
            char* r = (char*)malloc((size_t)n + i + 1);
            strcpy(r, s2);
            strcpy(r + n, s1 + (m - i));
            return r;
        }
    }
    char* r = (char*)malloc((size_t)m + n + 1);
    strcpy(r, s1);
    strcpy(r + m, s2);
    return r;
}
