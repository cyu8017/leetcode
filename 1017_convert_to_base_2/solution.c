// LeetCode 1017 - Convert to Base -2
// https://leetcode.com/problems/convert-to-base-2/

#include <stdlib.h>
#include <string.h>

char* baseNeg2(int n) {
    if (n == 0) {
        char* z = (char*)malloc(2);
        z[0] = '0'; z[1] = '\0';
        return z;
    }
    char buf[64];
    int len = 0;
    while (n) {
        int rem = n % -2;
        n /= -2;
        if (rem < 0) {
            n += 1;
            rem += 2;
        }
        buf[len++] = (char)('0' + rem);
    }
    char* ans = (char*)malloc((size_t)len + 1);
    for (int i = 0; i < len; i++) ans[i] = buf[len - 1 - i];
    ans[len] = '\0';
    return ans;
}
