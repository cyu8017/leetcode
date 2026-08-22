// LeetCode 3798 - Largest Even Number
// https://leetcode.com/problems/largest-even-number/

#include <stdlib.h>
#include <string.h>

char* largestEven(char* s) {
    int n = (int)strlen(s);
    while (n > 0 && s[n - 1] == '1') n--;
    char* out = (char*)malloc((size_t)n + 1);
    memcpy(out, s, (size_t)n);
    out[n] = '\0';
    return out;
}
