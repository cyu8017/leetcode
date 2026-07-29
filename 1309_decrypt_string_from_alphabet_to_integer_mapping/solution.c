// LeetCode 1309 - Decrypt String from Alphabet to Integer Mapping
// https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

#include <stdlib.h>
#include <string.h>

char* freqAlphabets(char* s) {
    int n = (int)strlen(s);
    char* tmp = (char*)malloc(n + 1);
    int t = 0;
    for (int i = n - 1; i >= 0; ) {
        if (s[i] == '#') {
            int v = (s[i - 2] - '0') * 10 + (s[i - 1] - '0');
            tmp[t++] = (char)('a' + v - 1);
            i -= 3;
        } else {
            tmp[t++] = (char)('a' + (s[i] - '0') - 1);
            i--;
        }
    }
    char* ans = (char*)malloc(t + 1);
    for (int i = 0; i < t; i++) ans[i] = tmp[t - 1 - i];
    ans[t] = '\0';
    free(tmp);
    return ans;
}
