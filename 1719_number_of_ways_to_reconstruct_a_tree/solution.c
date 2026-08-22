// LeetCode 1719 - Number Of Ways To Reconstruct A Tree
// https://leetcode.com/problems/number-of-ways-to-reconstruct-a-tree/

#include <stdbool.h>
#include <string.h>

#define MAX_NODE 501

int checkWays(int** pairs, int pairsSize, int* pairsColSize) {
    static bool adj[MAX_NODE][MAX_NODE];
    static int degree[MAX_NODE];
    static bool present[MAX_NODE];
    memset(adj, 0, sizeof(adj));
    memset(degree, 0, sizeof(degree));
    memset(present, 0, sizeof(present));

    for (int i = 0; i < pairsSize; i++) {
        int a = pairs[i][0];
        int b = pairs[i][1];
        if (!adj[a][b]) {
            adj[a][b] = true;
            adj[b][a] = true;
            degree[a]++;
            degree[b]++;
        }
        present[a] = true;
        present[b] = true;
    }
    int n = 0;
    for (int v = 1; v < MAX_NODE; v++) {
        if (present[v]) {
            n++;
        }
    }
    int root = -1;
    for (int v = 1; v < MAX_NODE; v++) {
        if (present[v] && degree[v] == n - 1) {
            root = v;
            break;
        }
    }
    if (root == -1) {
        return 0;
    }
    int ans = 1;
    for (int node = 1; node < MAX_NODE; node++) {
        if (!present[node] || node == root) {
            continue;
        }
        int parent = -1;
        int parentDegree = n + 1;
        for (int nei = 1; nei < MAX_NODE; nei++) {
            if (adj[node][nei] && degree[nei] >= degree[node] && degree[nei] < parentDegree) {
                parent = nei;
                parentDegree = degree[nei];
            }
        }
        if (parent == -1) {
            return 0;
        }
        for (int nei = 1; nei < MAX_NODE; nei++) {
            if (adj[node][nei] && nei != parent && !adj[parent][nei]) {
                return 0;
            }
        }
        if (degree[parent] == degree[node]) {
            ans = 2;
        }
    }
    return ans;
}
