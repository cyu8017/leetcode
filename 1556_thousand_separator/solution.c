// LeetCode 1556 - Thousand Separator
// https://leetcode.com/problems/thousand-separator/

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

char* thousandSeparator(int n) {
    char buf[32];
    sprintf(buf, "%d", n);
    int len = (int)strlen(buf);
    int dots = (len - 1) / 3;
    char* out = (char*)malloc((size_t)len + dots + 1);
    int j = 0;
    for (int i = 0; i < len; i++) {
        if (i && (len - i) % 3 == 0) out[j++] = '.';
        out[j++] = buf[i];
    }
    out[j] = '\0';
    return out;
}
