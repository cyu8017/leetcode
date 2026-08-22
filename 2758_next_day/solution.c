// LeetCode 2758 - Next Day
// https://leetcode.com/problems/next-day/

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

char* nextDay(char* date) {
    int y, m, d;
    sscanf(date, "%d-%d-%d", &y, &m, &d);
    d++;
    if (d > dim(y, m)) { d = 1; m++; }
    if (m > 12) { m = 1; y++; }
    char* r = (char*)malloc(16);
    sprintf(r, "%04d-%02d-%02d", y, m, d);
    return r;
}
