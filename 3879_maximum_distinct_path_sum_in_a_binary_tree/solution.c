// LeetCode 3879 - Maximum Distinct Path Sum In A Binary Tree
// https://leetcode.com/problems/maximum-distinct-path-sum-in-a-binary-tree/

#include <stdlib.h>
#include <limits.h>
#include <stdbool.h>
#include <string.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

enum { MAXN3879 = 512, VALMAX3879 = 100001 };

static struct TreeNode* nodes3879[MAXN3879];
static int ncnt3879;
static struct TreeNode* adj3879[MAXN3879][4];
static int deg3879[MAXN3879];
static bool vis3879[VALMAX3879];

static int idx3879(struct TreeNode* node) {
    for (int i = 0; i < ncnt3879; i++) if (nodes3879[i] == node) return i;
    return -1;
}

static void collect3879(struct TreeNode* node) {
    if (!node) return;
    nodes3879[ncnt3879++] = node;
    collect3879(node->left);
    collect3879(node->right);
}

static int dfs23879(struct TreeNode* node) {
    if (!node) return 0;
    int v = node->val;
    if (v >= 0 && v < VALMAX3879 && vis3879[v]) return 0;
    if (v >= 0 && v < VALMAX3879) vis3879[v] = true;
    int id = idx3879(node);
    int best = 0;
    for (int i = 0; i < deg3879[id]; i++) {
        int t = dfs23879(adj3879[id][i]);
        if (t > best) best = t;
    }
    if (v >= 0 && v < VALMAX3879) vis3879[v] = false;
    return v + best;
}

int maxSum(struct TreeNode* root) {
    if (!root) return 0;
    ncnt3879 = 0;
    collect3879(root);
    for (int i = 0; i < ncnt3879; i++) {
        deg3879[i] = 0;
        struct TreeNode* node = nodes3879[i];
        struct TreeNode* p = NULL;
        for (int j = 0; j < ncnt3879; j++) {
            if (nodes3879[j]->left == node || nodes3879[j]->right == node) { p = nodes3879[j]; break; }
        }
        if (p) adj3879[i][deg3879[i]++] = p;
        if (node->left) adj3879[i][deg3879[i]++] = node->left;
        if (node->right) adj3879[i][deg3879[i]++] = node->right;
    }
    int ans = INT_MIN;
    for (int i = 0; i < ncnt3879; i++) {
        memset(vis3879, 0, sizeof(vis3879));
        int t = dfs23879(nodes3879[i]);
        if (t > ans) ans = t;
    }
    return ans;
}
