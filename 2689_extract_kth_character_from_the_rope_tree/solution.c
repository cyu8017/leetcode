// LeetCode 2689 - Extract Kth Character From The Rope Tree
// https://leetcode.com/problems/extract-kth-character-from-the-rope-tree/

struct RopeTreeNode {
    int len;
    char val;
    struct RopeTreeNode* left;
    struct RopeTreeNode* right;
};

static char dfs2689(struct RopeTreeNode* node, int kk) {
    if (!node->left && !node->right) return node->val;
    int leftLen = 0;
    if (node->left) leftLen = node->left->len > 0 ? node->left->len : 1;
    if (kk <= leftLen) return dfs2689(node->left, kk);
    return dfs2689(node->right, kk - leftLen);
}

char getKthCharacter(struct RopeTreeNode* root, int k) {
    return dfs2689(root, k);
}
