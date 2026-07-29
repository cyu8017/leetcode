// LeetCode 1319 - Number of Operations to Make Network Connected
// https://leetcode.com/problems/number-of-operations-to-make-network-connected/

#include <stdlib.h>

static int findp(int* parent, int x) {
    while (x != parent[x]) { parent[x] = parent[parent[x]]; x = parent[x]; }
    return x;
}

int makeConnected(int n, int** connections, int connectionsSize, int* connectionsColSize) {
    (void)connectionsColSize;
    if (connectionsSize < n - 1) return -1;
    int* parent = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) parent[i] = i;
    for (int i = 0; i < connectionsSize; i++) {
        int ra = findp(parent, connections[i][0]);
        int rb = findp(parent, connections[i][1]);
        if (ra != rb) parent[ra] = rb;
    }
    int comps = 0;
    for (int i = 0; i < n; i++) if (findp(parent, i) == i) comps++;
    free(parent);
    return comps - 1;
}
