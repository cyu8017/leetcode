// LeetCode 0899 - Orderly Queue
// https://leetcode.com/problems/orderly-queue/

#include <stdlib.h>
#include <string.h>

static int cmp_char(const void* a, const void* b) {
    return *(const char*)a - *(const char*)b;
}

char* orderlyQueue(char* s, int k) {
    int n = (int)strlen(s);
    char* ans = (char*)malloc((size_t)n + 1);
    if (k > 1) {
        strcpy(ans, s);
        qsort(ans, (size_t)n, 1, cmp_char);
        return ans;
    }
    strcpy(ans, s);
    char* rot = (char*)malloc((size_t)n * 2 + 1);
    strcpy(rot, s);
    strcat(rot, s);
    for (int i = 1; i < n; i++) {
        if (strncmp(rot + i, ans, (size_t)n) < 0) {
            strncpy(ans, rot + i, (size_t)n);
            ans[n] = '\0';
        }
    }
    free(rot);
    return ans;
}
