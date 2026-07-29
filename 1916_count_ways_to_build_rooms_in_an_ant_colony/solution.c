// LeetCode 1916 - Count Ways to Build Rooms in an Ant Colony
// https://leetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony/

#include <stdlib.h>

static long long modPow(long long a, long long e, long long mod) {
    long long r = 1;
    while (e) {
        if (e & 1) r = r * a % mod;
        a = a * a % mod;
        e >>= 1;
    }
    return r;
}

static long long dfsWays(int node, int** children, int* childSize, long long* fact, long long* invFact, long long MOD, int* outSize) {
    int size = 0;
    long long ways = 1;
    for (int i = 0; i < childSize[node]; i++) {
        int child = children[node][i];
        int childSizeN = 0;
        long long childWays = dfsWays(child, children, childSize, fact, invFact, MOD, &childSizeN);
        ways = ways * childWays % MOD * fact[size + childSizeN] % MOD * invFact[childSizeN] % MOD * invFact[size] % MOD;
        size += childSizeN;
    }
    *outSize = size + 1;
    return ways;
}

int waysToBuildRooms(int* prevRoom, int prevRoomSize) {
    const long long MOD = 1000000007LL;
    int n = prevRoomSize;
    int** children = (int**)calloc((size_t)n, sizeof(int*));
    int* childCap = (int*)calloc((size_t)n, sizeof(int));
    int* childSize = (int*)calloc((size_t)n, sizeof(int));
    for (int room = 0; room < n; room++) {
        int prev = prevRoom[room];
        if (prev == -1) continue;
        if (childSize[prev] == childCap[prev]) {
            childCap[prev] = childCap[prev] ? childCap[prev] * 2 : 4;
            children[prev] = (int*)realloc(children[prev], (size_t)childCap[prev] * sizeof(int));
        }
        children[prev][childSize[prev]++] = room;
    }
    long long* fact = (long long*)malloc((size_t)(n + 1) * sizeof(long long));
    long long* invFact = (long long*)malloc((size_t)(n + 1) * sizeof(long long));
    fact[0] = 1;
    for (int i = 1; i <= n; i++) fact[i] = fact[i - 1] * i % MOD;
    invFact[n] = modPow(fact[n], MOD - 2, MOD);
    for (int i = n; i > 0; i--) invFact[i - 1] = invFact[i] * i % MOD;
    int sz = 0;
    int ans = (int)dfsWays(0, children, childSize, fact, invFact, MOD, &sz);
    for (int i = 0; i < n; i++) free(children[i]);
    free(children); free(childCap); free(childSize); free(fact); free(invFact);
    return ans;
}
