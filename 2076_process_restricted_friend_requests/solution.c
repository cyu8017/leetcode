// LeetCode 2076 - Process Restricted Friend Requests
// https://leetcode.com/problems/process-restricted-friend-requests/

#include <stdlib.h>
#include <stdbool.h>

static int find2076(int* parent, int x) {
    if (parent[x] != x) parent[x] = find2076(parent, parent[x]);
    return parent[x];
}

bool* friendRequests(int n, int** restrictions, int restrictionsSize, int* restrictionsColSize, int** requests, int requestsSize, int* requestsColSize, int* returnSize) {
    (void)restrictionsColSize; (void)requestsColSize;
    int* parent = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) parent[i] = i;
    bool* ans = (bool*)malloc((size_t)requestsSize * sizeof(bool));
    for (int i = 0; i < requestsSize; i++) {
        int u = find2076(parent, requests[i][0]);
        int v = find2076(parent, requests[i][1]);
        bool ok = true;
        if (u != v) {
            for (int j = 0; j < restrictionsSize; j++) {
                int x = find2076(parent, restrictions[j][0]);
                int y = find2076(parent, restrictions[j][1]);
                if ((x == u && y == v) || (x == v && y == u)) { ok = false; break; }
            }
        }
        ans[i] = ok;
        if (ok && u != v) parent[u] = v;
    }
    free(parent);
    *returnSize = requestsSize;
    return ans;
}
