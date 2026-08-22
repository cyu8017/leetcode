// LeetCode 3461 - Check If Digits Are Equal in String After Operations I
// https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

bool hasSameDigits(char* s) {
    int n = (int)strlen(s);
    char* b = (char*)malloc((size_t)n + 1);
    memcpy(b, s, (size_t)n + 1);
    int len = n;
    while (len > 2) {
        for (int i = 0; i + 1 < len; i++) {
            b[i] = (char)('0' + (b[i] - '0' + b[i + 1] - '0') % 10);
        }
        len--;
        b[len] = '\0';
    }
    bool ok = b[0] == b[1];
    free(b);
    return ok;
}
