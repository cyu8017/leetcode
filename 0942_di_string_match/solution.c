// LeetCode 0942 - DI String Match
// https://leetcode.com/problems/di-string-match/

#include <stdlib.h>
#include <string.h>

int* diStringMatch(char* s, int* returnSize) {
    int n = (int)strlen(s);
    int* ans = (int*)malloc((size_t)(n + 1) * sizeof(int));
    int lo = 0, hi = n, k = 0;
    for (int i = 0; i < n; i++) {
        if (s[i] == 'I') ans[k++] = lo++;
        else ans[k++] = hi--;
    }
    ans[k++] = lo;
    *returnSize = n + 1;
    return ans;
}
