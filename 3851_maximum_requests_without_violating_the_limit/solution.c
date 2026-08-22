// LeetCode 3851 - Maximum Requests Without Violating The Limit
// https://leetcode.com/problems/maximum-requests-without-violating-the-limit/

#include <stdlib.h>

typedef struct { int u; int* ts; int n, cap; } Group3851;

static int cmp_int(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

int maxRequests(int** requests, int requestsSize, int* requestsColSize, int k, int window) {
    (void)requestsColSize;
    Group3851* g = (Group3851*)calloc((size_t)requestsSize, sizeof(Group3851));
    int gsz = 0;
    for (int i = 0; i < requestsSize; i++) {
        int u = requests[i][0], t = requests[i][1];
        int idx = -1;
        for (int j = 0; j < gsz; j++) if (g[j].u == u) { idx = j; break; }
        if (idx < 0) { idx = gsz; g[gsz].u = u; g[gsz].ts = NULL; g[gsz].n = 0; g[gsz].cap = 0; gsz++; }
        if (g[idx].n == g[idx].cap) {
            g[idx].cap = g[idx].cap ? g[idx].cap * 2 : 4;
            g[idx].ts = (int*)realloc(g[idx].ts, (size_t)g[idx].cap * sizeof(int));
        }
        g[idx].ts[g[idx].n++] = t;
    }
    int ans = requestsSize;
    for (int gi = 0; gi < gsz; gi++) {
        qsort(g[gi].ts, (size_t)g[gi].n, sizeof(int), cmp_int);
        int* kept = (int*)malloc((size_t)g[gi].n * sizeof(int));
        int kn = 0, kh = 0;
        for (int i = 0; i < g[gi].n; i++) {
            int t = g[gi].ts[i];
            while (kn > kh && t - kept[kh] > window) kh++;
            if (kn - kh < k) kept[kn++] = t;
            else ans--;
        }
        free(kept);
        free(g[gi].ts);
    }
    free(g);
    return ans;
}
