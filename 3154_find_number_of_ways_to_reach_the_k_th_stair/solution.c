// LeetCode 3154 - Find Number of Ways to Reach the K-th Stair
// https://leetcode.com/problems/find-number-of-ways-to-reach-the-k-th-stair/

#include <stdlib.h>

enum { H3154 = 100003 };
typedef struct { long long key; int val; int used; } E3154;
static E3154 ht3154[H3154];
static int k3154;

static int dfs3154(int i, int j, int jump) {
    if (i > k3154 + 1) return 0;
    long long key = ((long long)i << 32) | ((long long)jump << 1) | j;
    unsigned h = (unsigned)(key % H3154);
    for (int t = 0; t < H3154; t++) {
        unsigned idx = (h + t) % H3154;
        if (!ht3154[idx].used) {
            int ans = 0;
            if (i == k3154) ans++;
            if (i > 0 && j == 0) ans += dfs3154(i - 1, 1, jump);
            ans += dfs3154(i + (1 << jump), 0, jump + 1);
            ht3154[idx].used = 1; ht3154[idx].key = key; ht3154[idx].val = ans;
            return ans;
        }
        if (ht3154[idx].key == key) return ht3154[idx].val;
    }
    return 0;
}

int waysToReachStair(int k) {
    k3154 = k;
    for (int i = 0; i < H3154; i++) ht3154[i].used = 0;
    return dfs3154(1, 0, 0);
}
