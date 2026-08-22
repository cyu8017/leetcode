// LeetCode 2612 - Minimum Reverse Operations
// https://leetcode.com/problems/minimum-reverse-operations/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* minReverseOperations(int n, int p, int* banned, int bannedSize, int k, int* returnSize) {
    bool* ban = (bool*)calloc((size_t)n, sizeof(bool));
    for (int i = 0; i < bannedSize; i++) ban[banned[i]] = true;
    int* ans = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) ans[i] = -1;
    ans[p] = 0;
    int* q = (int*)malloc((size_t)n * sizeof(int));
    int qh = 0, qt = 0;
    q[qt++] = p;
    while (qh < qt) {
        int cur = q[qh++];
        int lo = cur - (k - 1);
        if (lo < 0) lo = 0;
        int hi = cur;
        if (hi > n - k) hi = n - k;
        for (int L = lo; L <= hi; L++) {
            int R = L + k - 1;
            int ni = L + R - cur;
            if (ni < 0 || ni >= n || ban[ni] || ans[ni] != -1) continue;
            ans[ni] = ans[cur] + 1;
            q[qt++] = ni;
        }
    }
    free(ban); free(q);
    *returnSize = n;
    return ans;
}
