// LeetCode 2385 - Amount of Time for Binary Tree to Be Infected
// https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

typedef struct { int* data; int size; int cap; } Vec;

static void vecPush(Vec* v, int x) {
    if (v->size >= v->cap) {
        v->cap = v->cap ? v->cap * 2 : 4;
        v->data = (int*)realloc(v->data, (size_t)v->cap * sizeof(int));
    }
    v->data[v->size++] = x;
}

static void collect(struct TreeNode* node, int* vals, int* n) {
    if (!node) return;
    vals[(*n)++] = node->val;
    collect(node->left, vals, n);
    collect(node->right, vals, n);
}

static int idxOf(int* vals, int n, int v) {
    for (int i = 0; i < n; i++) if (vals[i] == v) return i;
    return -1;
}

static void build(struct TreeNode* node, struct TreeNode* parent, Vec* g, int* vals, int n) {
    if (!node) return;
    int u = idxOf(vals, n, node->val);
    if (parent) {
        int p = idxOf(vals, n, parent->val);
        vecPush(&g[u], p);
        vecPush(&g[p], u);
    }
    build(node->left, node, g, vals, n);
    build(node->right, node, g, vals, n);
}

int amountOfTime(struct TreeNode* root, int start) {
    int vals[100000], n = 0;
    collect(root, vals, &n);
    Vec* g = (Vec*)calloc((size_t)n, sizeof(Vec));
    build(root, NULL, g, vals, n);
    int startIdx = idxOf(vals, n, start);
    bool* vis = (bool*)calloc((size_t)n, sizeof(bool));
    int* qv = (int*)malloc((size_t)n * sizeof(int));
    int* qd = (int*)malloc((size_t)n * sizeof(int));
    int qh = 0, qt = 0;
    qv[qt] = startIdx; qd[qt] = 0; qt++;
    vis[startIdx] = true;
    int ans = 0;
    while (qh < qt) {
        int v = qv[qh], d = qd[qh]; qh++;
        if (d > ans) ans = d;
        for (int i = 0; i < g[v].size; i++) {
            int nxt = g[v].data[i];
            if (!vis[nxt]) { vis[nxt] = true; qv[qt] = nxt; qd[qt] = d + 1; qt++; }
        }
    }
    for (int i = 0; i < n; i++) free(g[i].data);
    free(g); free(vis); free(qv); free(qd);
    return ans;
}
