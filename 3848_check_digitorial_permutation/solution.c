// LeetCode 3848 - Check Digitorial Permutation
// https://leetcode.com/problems/check-digitorial-permutation/

#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

static int cmp_char(const void* a, const void* b) {
    return *(const char*)a - *(const char*)b;
}

bool isDigitorialPermutation(int n) {
    int f[10];
    f[0] = 1;
    for (int i = 1; i < 10; i++) f[i] = f[i - 1] * i;
    int x = 0, y = n;
    while (y > 0) { x += f[y % 10]; y /= 10; }
    char a[32], b[32];
    sprintf(a, "%d", x);
    sprintf(b, "%d", n);
    int la = (int)strlen(a), lb = (int)strlen(b);
    if (la != lb) return false;
    qsort(a, (size_t)la, 1, cmp_char);
    qsort(b, (size_t)lb, 1, cmp_char);
    return strcmp(a, b) == 0;
}
