// LeetCode 1433 - Check If a String Can Break Another String
// https://leetcode.com/problems/check-if-a-string-can-break-another-string/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

static int cmp_char(const void* a, const void* b) { return *(const char*)a - *(const char*)b; }

bool checkIfCanBreak(char* s1, char* s2) {
    int n = (int)strlen(s1);
    char* a = (char*)malloc(n + 1); char* b = (char*)malloc(n + 1);
    strcpy(a, s1); strcpy(b, s2);
    qsort(a, n, 1, cmp_char); qsort(b, n, 1, cmp_char);
    int ge = 1, le = 1;
    for (int i = 0; i < n; i++) {
        if (a[i] < b[i]) ge = 0;
        if (a[i] > b[i]) le = 0;
    }
    free(a); free(b);
    return ge || le;
}
