// LeetCode 3939 - Count Non Adjacent Subsets in a Rooted Tree
// https://leetcode.com/problems/count-non-adjacent-subsets-in-a-rooted-tree/

#include <stdlib.h>
#include <string.h>

enum { MOD3939 = 1000000007LL };

int countNonAdjacentSubsets(int* parent, int parentSize, int* nums, int numsSize, int k) {
    (void)numsSize;
    int n = parentSize;
    int** children = calloc((size_t)n, sizeof(int*));
    int* deg = calloc((size_t)n, sizeof(int));
    int* cap = calloc((size_t)n, sizeof(int));
    for (int i = 1; i < n; i++) {
        int p = parent[i];
        if (deg[p] == cap[p]) { cap[p] = cap[p] ? cap[p] * 2 : 4; children[p] = realloc(children[p], (size_t)cap[p] * sizeof(int)); }
        children[p][deg[p]++] = i;
    }
    long long** dp0 = malloc((size_t)n * sizeof(long long*));
    long long** dp1 = malloc((size_t)n * sizeof(long long*));
    for (int u = n - 1; u >= 0; u--) {
        long long* a = calloc((size_t)k, sizeof(long long));
        long long* b = calloc((size_t)k, sizeof(long long));
        a[0] = 1;
        b[((nums[u] % k) + k) % k] = 1;
        for (int ci = 0; ci < deg[u]; ci++) {
            int v = children[u][ci];
            long long* na = calloc((size_t)k, sizeof(long long));
            long long* nb = calloc((size_t)k, sizeof(long long));
            for (int x = 0; x < k; x++) {
                for (int y = 0; y < k; y++) {
                    long long allChild = (dp0[v][y] + dp1[v][y]) % MOD3939;
                    na[(x + y) % k] = (na[(x + y) % k] + a[x] * allChild) % MOD3939;
                    nb[(x + y) % k] = (nb[(x + y) % k] + b[x] * dp0[v][y]) % MOD3939;
                }
            }
            free(a); free(b);
            a = na; b = nb;
        }
        dp0[u] = a; dp1[u] = b;
    }
    long long ans = (dp0[0][0] + dp1[0][0] - 1) % MOD3939;
    if (ans < 0) ans += MOD3939;
    for (int i = 0; i < n; i++) { free(children[i]); free(dp0[i]); free(dp1[i]); }
    free(children); free(deg); free(cap); free(dp0); free(dp1);
    return (int)ans;
}
