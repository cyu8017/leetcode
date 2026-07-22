// LeetCode 1694 - Reformat Phone Number
// https://leetcode.com/problems/reformat-phone-number/

#include <stdlib.h>
#include <string.h>
#include <ctype.h>

char* reformatNumber(char* number) {
    char digits[120];
    int n = 0;
    for (char* p = number; *p; p++) if (isdigit((unsigned char)*p)) digits[n++] = *p;
    digits[n] = '\0';
    char* out = (char*)malloc(160);
    int j = 0, i = 0;
    while (n - i > 4) {
        out[j++] = digits[i++]; out[j++] = digits[i++]; out[j++] = digits[i++];
        out[j++] = '-';
    }
    int rem = n - i;
    if (rem == 4) {
        out[j++] = digits[i++]; out[j++] = digits[i++];
        out[j++] = '-';
        out[j++] = digits[i++]; out[j++] = digits[i++];
    } else {
        while (i < n) out[j++] = digits[i++];
    }
    out[j] = '\0';
    return out;
}
