// LeetCode 2059 - Minimum Operations to Convert Number
// https://leetcode.com/problems/minimum-operations-to-convert-number/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

int minimumOperations(int* nums, int numsSize, int start, int goal) {
    if (start == goal) return 0;
    bool vis[1001];
    memset(vis, 0, sizeof(vis));
    int* q = (int*)malloc(1001 * sizeof(int));
    int qh = 0, qt = 0;
    q[qt++] = start;
    vis[start] = true;
    int steps = 0;
    while (qh < qt) {
        steps++;
        int sz = qt - qh;
        for (int s = 0; s < sz; s++) {
            int cur = q[qh++];
            for (int i = 0; i < numsSize; i++) {
                int x = nums[i];
                int nxts[3] = {cur + x, cur - x, cur ^ x};
                for (int t = 0; t < 3; t++) {
                    int nxt = nxts[t];
                    if (nxt == goal) { free(q); return steps; }
                    if (nxt >= 0 && nxt <= 1000 && !vis[nxt]) {
                        vis[nxt] = true;
                        q[qt++] = nxt;
                    }
                }
            }
        }
    }
    free(q);
    return -1;
}
