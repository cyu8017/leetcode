// LeetCode 2375 - Construct Smallest Number From DI String
// https://leetcode.com/problems/construct-smallest-number-from-di-string/

#include <stdlib.h>
#include <string.h>

char* smallestNumber(char* pattern) {
    int n = (int)strlen(pattern);
    char* ans = (char*)malloc((size_t)(n + 2));
    for (int i = 0; i <= n; i++) ans[i] = (char)('1' + i);
    ans[n + 1] = '\0';
    int i = 0;
    while (i < n) {
        if (pattern[i] == 'I') { i++; continue; }
        int j = i;
        while (j < n && pattern[j] == 'D') j++;
        int l = i, r = j;
        while (l < r) { char t = ans[l]; ans[l] = ans[r]; ans[r] = t; l++; r--; }
        i = j;
    }
    return ans;
}
