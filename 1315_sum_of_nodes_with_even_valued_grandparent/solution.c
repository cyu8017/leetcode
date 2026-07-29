// LeetCode 1315 - Sum of Nodes with Even-Valued Grandparent
// https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

static int dfs(struct TreeNode* node, struct TreeNode* parent, struct TreeNode* grandparent) {
    if (!node) return 0;
    int add = (grandparent && grandparent->val % 2 == 0) ? node->val : 0;
    return add + dfs(node->left, node, parent) + dfs(node->right, node, parent);
}

int sumEvenGrandparent(struct TreeNode* root) {
    return dfs(root, NULL, NULL);
}
