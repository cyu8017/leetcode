// LeetCode 1145 - Binary Tree Coloring Game
// https://leetcode.com/problems/binary-tree-coloring-game/

#include <stdbool.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

static int leftCnt, rightCnt;

static int dfsCount(struct TreeNode* node, int x) {
    if (!node) return 0;
    int l = dfsCount(node->left, x);
    int r = dfsCount(node->right, x);
    if (node->val == x) { leftCnt = l; rightCnt = r; }
    return l + r + 1;
}

bool btreeGameWinningMove(struct TreeNode* root, int n, int x) {
    leftCnt = rightCnt = 0;
    dfsCount(root, x);
    int parentSide = n - leftCnt - rightCnt - 1;
    int best = leftCnt;
    if (rightCnt > best) best = rightCnt;
    if (parentSide > best) best = parentSide;
    return best > n / 2;
}
