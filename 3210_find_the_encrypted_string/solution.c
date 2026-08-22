// LeetCode 3210 - Find the Encrypted String
// https://leetcode.com/problems/find-the-encrypted-string/

#include <stdlib.h>
#include <string.h>

char* getEncryptedString(char* s, int k) {
    int n = (int)strlen(s);
    char* cs = malloc(n + 1);
    for (int i = 0; i < n; i++) cs[i] = s[(i + k) % n];
    cs[n] = 0;
    return cs;
}
