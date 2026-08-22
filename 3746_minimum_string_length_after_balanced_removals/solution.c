// LeetCode 3746 - Minimum String Length After Balanced Removals
// https://leetcode.com/problems/minimum-string-length-after-balanced-removals/

#include <string.h>

int minLengthAfterRemovals(char* s) {
    int a = 0, n = (int)strlen(s);
    for (int i = 0; i < n; i++) if (s[i] == 'a') a++;
    int b = n - a;
    int d = a - b;
    return d < 0 ? -d : d;
}
