// LeetCode 2777 - Date Range Generator
// https://leetcode.com/problems/date-range-generator/

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

static int isLeap(int y) {
    return (y % 4 == 0 && y % 100 != 0) || (y % 400 == 0);
}
static int dim(int y, int m) {
    static int d[] = {0,31,28,31,30,31,30,31,31,30,31,30,31};
    if (m == 2 && isLeap(y)) return 29;
    return d[m];
}
static void addDays(int* y, int* m, int* d, int step) {
    *d += step;
    while (*d > dim(*y, *m)) {
        *d -= dim(*y, *m);
        (*m)++;
        if (*m > 12) { *m = 1; (*y)++; }
    }
}
static long long toDays(int y, int m, int d) {
    long long days = 0;
    for (int yy = 1970; yy < y; yy++) days += isLeap(yy) ? 366 : 365;
    for (int mm = 1; mm < m; mm++) days += dim(y, mm);
    return days + d;
}

char** dateRangeGenerator(char* start, char* end, int step, int* returnSize) {
    int y1, m1, d1, y2, m2, d2;
    if (sscanf(start, "%d-%d-%d", &y1, &m1, &d1) != 3 ||
        sscanf(end, "%d-%d-%d", &y2, &m2, &d2) != 3) {
        *returnSize = 0;
        return NULL;
    }
    int cap = 64, sz = 0;
    char** ans = (char**)malloc(cap * sizeof(char*));
    long long endDays = toDays(y2, m2, d2);
    while (toDays(y1, m1, d1) <= endDays) {
        if (sz == cap) { cap *= 2; ans = (char**)realloc(ans, cap * sizeof(char*)); }
        ans[sz] = (char*)malloc(16);
        sprintf(ans[sz], "%04d-%02d-%02d", y1, m1, d1);
        sz++;
        addDays(&y1, &m1, &d1, step);
    }
    *returnSize = sz;
    return ans;
}
