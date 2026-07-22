// LeetCode 1663 - Smallest String With A Given Numeric Value
// https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/

#include <stdlib.h>
#include <string.h>

char* getSmallestString(int n, int k) {
    char* a = (char*)malloc((size_t)n + 1);
    memset(a, 'a', (size_t)n);
    a[n] = '\0';
    k -= n;
    for (int i = n - 1; i >= 0 && k > 0; i--) {
        int d = k < 25 ? k : 25;
        a[i] = (char)('a' + d);
        k -= d;
    }
    return a;
}
