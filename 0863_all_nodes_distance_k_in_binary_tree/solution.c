// LeetCode 0863 - All Nodes Distance K in Binary Tree
// https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

#include <stdlib.h>
#include <stdbool.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

typedef struct TreeNode Node;

static Node* nodes[501];
static Node* parent[501];
static int ncount;

static void build(Node* node, Node* p) {
    if (!node) return;
    nodes[ncount] = node;
    parent[ncount] = p;
    ncount++;
    build(node->left, node);
    build(node->right, node);
}

static int find_idx(Node* node) {
    for (int i = 0; i < ncount; i++) if (nodes[i] == node) return i;
    return -1;
}

int* distanceK(struct TreeNode* root, struct TreeNode* target, int k, int* returnSize) {
    ncount = 0;
    build(root, NULL);
    bool* seen = (bool*)calloc((size_t)ncount, sizeof(bool));
    int* q = (int*)malloc((size_t)ncount * sizeof(int));
    int* dist = (int*)malloc((size_t)ncount * sizeof(int));
    int qh = 0, qt = 0;
    int ti = find_idx(target);
    q[qt] = ti; dist[qt] = 0; qt++;
    seen[ti] = true;
    int* ans = (int*)malloc((size_t)ncount * sizeof(int));
    int ac = 0;
    while (qh < qt) {
        int idx = q[qh];
        int d = dist[qh];
        qh++;
        if (d == k) {
            ans[ac++] = nodes[idx]->val;
            continue;
        }
        Node* cur = nodes[idx];
        Node* neigh[3];
        int nn = 0;
        if (cur->left) neigh[nn++] = cur->left;
        if (cur->right) neigh[nn++] = cur->right;
        if (parent[idx]) neigh[nn++] = parent[idx];
        for (int i = 0; i < nn; i++) {
            int ni = find_idx(neigh[i]);
            if (!seen[ni]) {
                seen[ni] = true;
                q[qt] = ni; dist[qt] = d + 1; qt++;
            }
        }
    }
    free(seen); free(q); free(dist);
    *returnSize = ac;
    return ans;
}
