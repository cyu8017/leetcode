// LeetCode 3602 - Hexadecimal and Hexatrigesimal Conversion
// https://leetcode.com/problems/hexadecimal-and-hexatrigesimal-conversion/

#include <stdlib.h>
#include <string.h>

static void conv(int x, int k, char* out) {
    char tmp[64]; int n = 0;
    if (x == 0) { out[0] = '0'; out[1] = 0; return; }
    while (x > 0) {
        int v = x % k;
        tmp[n++] = (char)(v <= 9 ? '0' + v : 'A' + v - 10);
        x /= k;
    }
    for (int i = 0; i < n; i++) out[i] = tmp[n - 1 - i];
    out[n] = 0;
}

char* concatHex36(int n) {
    char a[64], b[64];
    conv(n * n, 16, a);
    conv(n * n * n, 36, b);
    char* r = (char*)malloc(strlen(a) + strlen(b) + 1);
    strcpy(r, a); strcat(r, b);
    return r;
}
