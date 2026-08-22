// LeetCode 3161 - Block Placement Queries
// https://leetcode.com/problems/block-placement-queries/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

typedef struct { int* vals; int n; } FT3161;

static void ft_max(FT3161* ft, int i, int val) {
    for (; i < ft->n; i += i & -i)
        if (val > ft->vals[i]) ft->vals[i] = val;
}
static int ft_get(FT3161* ft, int i) {
    int res = 0;
    for (; i > 0; i -= i & -i)
        if (ft->vals[i] > res) res = ft->vals[i];
    return res;
}
static int lower_bound(int* a, int n, int x) {
    int lo = 0, hi = n;
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        if (a[mid] < x) lo = mid + 1; else hi = mid;
    }
    return lo;
}

bool* getResults(int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)queriesColSize;
    int n = queriesSize * 3;
    if (n > 50000) n = 50000;
    FT3161 tree = {calloc(n + 2, sizeof(int)), n + 2};
    int* obs = malloc((queriesSize + 2) * sizeof(int));
    int on = 2;
    obs[0] = 0; obs[1] = n;
    for (int i = 0; i < queriesSize; i++) {
        if (queries[i][0] == 1) {
            int x = queries[i][1];
            int j = lower_bound(obs, on, x);
            if (j == on || obs[j] != x) {
                for (int t = on; t > j; t--) obs[t] = obs[t - 1];
                obs[j] = x; on++;
            }
        }
    }
    for (int i = 0; i + 1 < on; i++) ft_max(&tree, obs[i + 1], obs[i + 1] - obs[i]);
    bool* tmp = malloc(queriesSize * sizeof(bool));
    int tn = 0;
    for (int i = queriesSize - 1; i >= 0; i--) {
        int typ = queries[i][0], x = queries[i][1];
        if (typ == 1) {
            int j = lower_bound(obs, on, x);
            int prev = obs[j - 1], next = obs[j + 1];
            for (int t = j; t + 1 < on; t++) obs[t] = obs[t + 1];
            on--;
            ft_max(&tree, next, next - prev);
        } else {
            int sz = queries[i][2];
            int j = lower_bound(obs, on, x + 1) - 1;
            int prev = obs[j];
            tmp[tn++] = ft_get(&tree, prev) >= sz || x - prev >= sz;
        }
    }
    bool* ans = malloc(tn * sizeof(bool));
    for (int i = 0; i < tn; i++) ans[i] = tmp[tn - 1 - i];
    free(tmp); free(obs); free(tree.vals);
    *returnSize = tn;
    return ans;
}
