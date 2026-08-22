// LeetCode 3327 - Check DFS Strings Are Palindromes
// https://leetcode.com/problems/check-if-dfs-strings-are-palindromes/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

static bool isPal(const char* s, int n) {
    for (int i = 0, j = n - 1; i < j; i++, j--) if (s[i] != s[j]) return false;
    return true;
}

static char* dfsStr(int u, int** g, int* glen, char* s, bool* ans) {
    int cap = 16, len = 0;
    char* out = (char*)malloc((size_t)cap);
    for (int i = 0; i < glen[u]; i++) {
        char* sub = dfsStr(g[u][i], g, glen, s, ans);
        int sl = (int)strlen(sub);
        while (len + sl + 2 > cap) { cap *= 2; out = realloc(out, (size_t)cap); }
        memcpy(out + len, sub, (size_t)sl);
        len += sl;
        free(sub);
    }
    if (len + 2 > cap) { cap = len + 2; out = realloc(out, (size_t)cap); }
    out[len++] = s[u];
    out[len] = 0;
    ans[u] = isPal(out, len);
    return out;
}

bool* findAnswer(int* parent, int parentSize, char* s, int* returnSize) {
    int n = parentSize;
    int** g = (int**)calloc((size_t)n, sizeof(int*));
    int* glen = (int*)calloc((size_t)n, sizeof(int));
    int* gcap = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) { gcap[i] = 4; g[i] = (int*)malloc(4 * sizeof(int)); }
    for (int i = 1; i < n; i++) {
        int p = parent[i];
        if (glen[p] == gcap[p]) { gcap[p] *= 2; g[p] = realloc(g[p], (size_t)gcap[p] * sizeof(int)); }
        g[p][glen[p]++] = i;
    }
    bool* ans = (bool*)calloc((size_t)n, sizeof(bool));
    free(dfsStr(0, g, glen, s, ans));
    for (int i = 0; i < n; i++) free(g[i]);
    free(g); free(glen); free(gcap);
    *returnSize = n;
    return ans;
}
