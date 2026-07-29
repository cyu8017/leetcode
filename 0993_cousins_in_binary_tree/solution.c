// LeetCode 0993 - Cousins in Binary Tree
// https://leetcode.com/problems/cousins-in-binary-tree/

#include <stdbool.h>
#include <stddef.h>

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

static int dx, dy;
static struct TreeNode *px, *py;
static int X, Y;

static void dfs(struct TreeNode* node, struct TreeNode* parent, int depth) {
    if (!node) return;
    if (node->val == X) { dx = depth; px = parent; }
    if (node->val == Y) { dy = depth; py = parent; }
    dfs(node->left, node, depth + 1);
    dfs(node->right, node, depth + 1);
}

bool isCousins(struct TreeNode* root, int x, int y) {
    X = x; Y = y; px = py = NULL;
    dfs(root, NULL, 0);
    return dx == dy && px != py;
}
