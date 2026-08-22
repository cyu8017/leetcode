// LeetCode 3441 - Minimum Cost Good Caption
// https://leetcode.com/problems/minimum-cost-good-caption/

#include <stdlib.h>
#include <string.h>

char* minCostGoodCaption(char* caption) {
    int n = (int)strlen(caption);
    if (n < 3) { char* r = (char*)malloc(1); r[0] = 0; return r; }
    char* ans = (char*)malloc(n + 1); memcpy(ans, caption, n); ans[n] = 0;
    int i = 0;
    while (i < n) {
        int j = i; while (j < n && ans[j] == ans[i]) j++;
        if (j - i >= 3) { i = j; continue; }
        int need = 3 - (j - i);
        if (j + need <= n) {
            for (int t = 0; t < need; t++) ans[j + t] = ans[i];
            i = j + need;
        } else {
            char ch = 'a';
            if (i > 0) ch = ans[i - 1];
            else if (j < n) ch = caption[j];
            for (int t = i; t < n; t++) ans[t] = ch;
            break;
        }
    }
    i = 0;
    while (i < n) {
        int j = i; while (j < n && ans[j] == ans[i]) j++;
        if (j - i < 3) { free(ans); char* r = (char*)malloc(1); r[0] = 0; return r; }
        i = j;
    }
    return ans;
}
