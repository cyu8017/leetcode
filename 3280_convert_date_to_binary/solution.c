// LeetCode 3280 - Convert Date to Binary
// https://leetcode.com/problems/convert-date-to-binary/

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

static void toBin(int v, char* buf) {
    if (v == 0) { buf[0] = '0'; buf[1] = 0; return; }
    char tmp[40]; int n = 0;
    while (v > 0) { tmp[n++] = (char)('0' + (v & 1)); v >>= 1; }
    for (int i = 0; i < n; i++) buf[i] = tmp[n - 1 - i];
    buf[n] = 0;
}

char* convertDateToBinary(char* date) {
    int y, m, d;
    sscanf(date, "%d-%d-%d", &y, &m, &d);
    char by[40], bm[40], bd[40];
    toBin(y, by); toBin(m, bm); toBin(d, bd);
    char* out = (char*)malloc(120);
    sprintf(out, "%s-%s-%s", by, bm, bd);
    return out;
}
