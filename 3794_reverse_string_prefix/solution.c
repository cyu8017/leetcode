// LeetCode 3794 - Reverse String Prefix
// https://leetcode.com/problems/reverse-string-prefix/

#include <stdlib.h>
#include <string.h>

char* reversePrefix(char* s, int k) {
    int n = (int)strlen(s);
    char* out = (char*)malloc((size_t)n + 1);
    memcpy(out, s, (size_t)n + 1);
    if (k > n) k = n;
    for (int l = 0, r = k - 1; l < r; l++, r--) {
        char t = out[l]; out[l] = out[r]; out[r] = t;
    }
    return out;
}
