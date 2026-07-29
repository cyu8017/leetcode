// LeetCode 0842 - Split Array into Fibonacci Sequence
// https://leetcode.com/problems/split-array-into-fibonacci-sequence/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

static int path[50], plen, n;
static const char* num;

static bool dfs(int start) {
    if (start == n) return plen >= 3;
    long long val = 0;
    for (int end = start; end < n; end++) {
        if (num[start] == '0' && end > start) break;
        val = val * 10 + (num[end] - '0');
        if (val > 2147483647LL) break;
        if (plen >= 2) {
            long long total = (long long)path[plen - 1] + path[plen - 2];
            if (val < total) continue;
            if (val > total) break;
        }
        path[plen++] = (int)val;
        if (dfs(end + 1)) return true;
        plen--;
    }
    return false;
}

int* splitIntoFibonacci(char* numStr, int* returnSize) {
    num = numStr;
    n = (int)strlen(numStr);
    plen = 0;
    dfs(0);
    int* ans = (int*)malloc((size_t)plen * sizeof(int) + 1);
    for (int i = 0; i < plen; i++) ans[i] = path[i];
    *returnSize = plen;
    return ans;
}
