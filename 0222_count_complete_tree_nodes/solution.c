// LeetCode 0222 - Count Complete Tree Nodes
// https://leetcode.com/problems/count-complete-tree-nodes/

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

static int leftDepth(struct TreeNode* node) {
    int depth = 0;
    while (node) {
        depth++;
        node = node->left;
    }
    return depth;
}

static int rightDepth(struct TreeNode* node) {
    int depth = 0;
    while (node) {
        depth++;
        node = node->right;
    }
    return depth;
}

int countNodes(struct TreeNode* root) {
    if (!root) {
        return 0;
    }
    int left = leftDepth(root);
    int right = rightDepth(root);
    if (left == right) {
        return (1 << left) - 1;
    }
    return 1 + countNodes(root->left) + countNodes(root->right);
}
