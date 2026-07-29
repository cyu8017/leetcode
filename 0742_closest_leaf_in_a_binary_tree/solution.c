// LeetCode 0742 - Closest Leaf in a Binary Tree
// https://leetcode.com/problems/closest-leaf-in-a-binary-tree/

#include <stdlib.h>
#include <stdbool.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

typedef struct {
    int* adj[1001];
    int deg[1001];
    bool leaf[1001];
    bool seen_node[1001];
} Graph;

static void addEdge(Graph* g, int a, int b) {
    g->adj[a] = (int*)realloc(g->adj[a], (size_t)(g->deg[a] + 1) * sizeof(int));
    g->adj[a][g->deg[a]++] = b;
    g->adj[b] = (int*)realloc(g->adj[b], (size_t)(g->deg[b] + 1) * sizeof(int));
    g->adj[b][g->deg[b]++] = a;
}

static void build(Graph* g, struct TreeNode* node, struct TreeNode* parent) {
    if (!node) {
        return;
    }
    g->seen_node[node->val] = true;
    if (parent) {
        addEdge(g, node->val, parent->val);
    }
    if (!node->left && !node->right) {
        g->leaf[node->val] = true;
    }
    build(g, node->right, node);
    build(g, node->left, node);
}

int findClosestLeaf(struct TreeNode* root, int k) {
    Graph g = {0};
    build(&g, root, NULL);
    int queue[1001];
    bool seen[1001] = {0};
    int head = 0, tail = 0;
    queue[tail++] = k;
    seen[k] = true;
    while (head < tail) {
        int value = queue[head++];
        if (g.leaf[value]) {
            for (int i = 0; i < 1001; i++) {
                free(g.adj[i]);
            }
            return value;
        }
        for (int i = 0; i < g.deg[value]; i++) {
            int nei = g.adj[value][i];
            if (!seen[nei]) {
                seen[nei] = true;
                queue[tail++] = nei;
            }
        }
    }
    for (int i = 0; i < 1001; i++) {
        free(g.adj[i]);
    }
    return -1;
}
