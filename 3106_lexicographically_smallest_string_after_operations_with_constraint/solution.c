// LeetCode 3106 - Lexicographically Smallest String After Operations With Constraint
// https://leetcode.com/problems/lexicographically-smallest-string-after-operations-with-constraint/

#include <stdlib.h>
#include <string.h>

char* getSmallestString(char* s, int k) {
    int n = (int)strlen(s);
    char* cs = (char*)malloc((size_t)n + 1);
    memcpy(cs, s, (size_t)n + 1);
    for (int i = 0; i < n; i++) {
        unsigned char c1 = (unsigned char)cs[i];
        for (unsigned char c2 = 'a'; c2 < c1; c2++) {
            int d1 = c1 - c2, d2 = 26 - c1 + c2;
            int d = d1 < d2 ? d1 : d2;
            if (d <= k) {
                cs[i] = (char)c2;
                k -= d;
                break;
            }
        }
    }
    return cs;
}
