// LeetCode 3216 - Lexicographically Smallest String After a Swap
// https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap/

#include <stdlib.h>
#include <string.h>

char* getSmallestString(char* s) {
    int n = (int)strlen(s);
    char* cs = malloc(n + 1);
    memcpy(cs, s, n + 1);
    for (int i = 1; i < n; i++) {
        unsigned char a = cs[i - 1], b = cs[i];
        if (a > b && a % 2 == b % 2) {
            cs[i - 1] = b; cs[i] = a;
            return cs;
        }
    }
    return cs;
}
