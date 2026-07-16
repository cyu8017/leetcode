// LeetCode 0547 - Number of Provinces
// https://leetcode.com/problems/number-of-provinces/

#include <stdlib.h>

static int find(int* parent, int node) {
    while (parent[node] != node) {
        parent[node] = parent[parent[node]];
        node = parent[node];
    }
    return node;
}

static void unite(int* parent, int left, int right) {
    const int rootLeft = find(parent, left);
    const int rootRight = find(parent, right);
    if (rootLeft != rootRight) {
        parent[rootRight] = rootLeft;
    }
}

int findCircleNum(int** isConnected, int isConnectedSize, int* isConnectedColSize) {
    const int n = isConnectedSize;
    int* parent = (int*)malloc((size_t)n * sizeof(int));
    for (int index = 0; index < n; index++) {
        parent[index] = index;
    }

    for (int row = 0; row < n; row++) {
        for (int col = row + 1; col < n; col++) {
            if (isConnected[row][col]) {
                unite(parent, row, col);
            }
        }
    }

    int provinces = 0;
    for (int index = 0; index < n; index++) {
        if (find(parent, index) == index) {
            provinces += 1;
        }
    }

    free(parent);
    return provinces;
}
