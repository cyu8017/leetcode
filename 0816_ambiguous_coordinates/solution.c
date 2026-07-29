// LeetCode 0816 - Ambiguous Coordinates
// https://leetcode.com/problems/ambiguous-coordinates/

#include <stdlib.h>
#include <string.h>
#include <stdio.h>

static int candidates(const char* frag, int len, char out[][32]) {
    int n = 0;
    if (len == 0) return 0;
    if (len > 1 && frag[0] == '0' && frag[len - 1] == '0') return 0;
    if (frag[0] == '0' && len > 1) {
        if (frag[len - 1] != '0') {
            out[n][0] = '0'; out[n][1] = '.';
            memcpy(out[n] + 2, frag + 1, (size_t)(len - 1));
            out[n][len + 1] = '\0';
            n++;
        }
        return n;
    }
    memcpy(out[n], frag, (size_t)len);
    out[n][len] = '\0';
    n++;
    if (frag[len - 1] == '0') return n;
    for (int i = 1; i < len; i++) {
        memcpy(out[n], frag, (size_t)i);
        out[n][i] = '.';
        memcpy(out[n] + i + 1, frag + i, (size_t)(len - i));
        out[n][len + 1] = '\0';
        n++;
    }
    return n;
}

char** ambiguousCoordinates(char* s, int* returnSize) {
    int dlen = (int)strlen(s) - 2;
    char digits[20];
    memcpy(digits, s + 1, (size_t)dlen);
    digits[dlen] = '\0';
    char** ans = (char**)malloc(2000 * sizeof(char*));
    int count = 0;
    char left[64][32], right[64][32];
    for (int i = 1; i < dlen; i++) {
        int nl = candidates(digits, i, left);
        int nr = candidates(digits + i, dlen - i, right);
        for (int a = 0; a < nl; a++) {
            for (int b = 0; b < nr; b++) {
                ans[count] = (char*)malloc(64);
                sprintf(ans[count], "(%s, %s)", left[a], right[b]);
                count++;
            }
        }
    }
    *returnSize = count;
    return ans;
}
