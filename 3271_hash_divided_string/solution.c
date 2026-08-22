// LeetCode 3271 - Hash Divided String
// https://leetcode.com/problems/hash-divided-string/

#include <stdlib.h>
#include <string.h>

char* stringHash(char* s, int k) {
    int n = (int)strlen(s);
    int outn = n / k;
    char* out = (char*)malloc((size_t)outn + 1);
    int oi = 0;
    for (int i = 0; i < n; i += k) {
        int sum = 0;
        for (int j = i; j < i + k; j++) sum += s[j] - 'a';
        out[oi++] = (char)('a' + sum % 26);
    }
    out[oi] = 0;
    return out;
}
