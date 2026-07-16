// LeetCode 0323 - Number of Connected Components in an Undirected Graph
// https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

static int findRoot(int* parent, int node) {
    if (parent[node] != node) {
        parent[node] = findRoot(parent, parent[node]);
    }
    return parent[node];
}

int countComponents(int n, int** edges, int edgesSize, int* edgesColSize) {
    (void)edgesColSize;
    int* parent = (int*)malloc((size_t)n * sizeof(int));
    int* rank = (int*)calloc((size_t)n, sizeof(int));
    for (int node = 0; node < n; node++) {
        parent[node] = node;
    }

    int components = n;
    for (int index = 0; index < edgesSize; index++) {
        int left = edges[index][0];
        int right = edges[index][1];
        int rootLeft = findRoot(parent, left);
        int rootRight = findRoot(parent, right);
        if (rootLeft == rootRight) {
            continue;
        }
        if (rank[rootLeft] < rank[rootRight]) {
            int tmp = rootLeft;
            rootLeft = rootRight;
            rootRight = tmp;
        }
        parent[rootRight] = rootLeft;
        if (rank[rootLeft] == rank[rootRight]) {
            rank[rootLeft] += 1;
        }
        components -= 1;
    }

    free(parent);
    free(rank);
    return components;
}
