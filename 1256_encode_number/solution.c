// LeetCode 1256 - Encode Number
// https://leetcode.com/problems/encode-number/

#include <stdlib.h>
#include <string.h>

char* encode(int num) {
    unsigned value = (unsigned)num + 1;
    char bits[33];
    int len = 0;
    while (value) {
        bits[len++] = (char)('0' + (value & 1));
        value >>= 1;
    }
    char* ans = (char*)malloc((size_t)len + 1);
    for (int i = 0; i < len; i++) ans[i] = bits[len - 1 - i];
    ans[len] = '\0';
    return ans;
}
