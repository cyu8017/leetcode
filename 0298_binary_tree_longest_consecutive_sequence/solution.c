// LeetCode 0298 - Binary Tree Longest Consecutive Sequence
// https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

static int maxInt(int left, int right) {
    return left > right ? left : right;
}

static int dfs(struct TreeNode* node, struct TreeNode* parent, int length) {
    if (node == NULL) {
        return 0;
    }

    int current = (parent != NULL && parent->val + 1 == node->val) ? length + 1 : 1;
    return maxInt(current, maxInt(dfs(node->left, node, current), dfs(node->right, node, current)));
}

int longestConsecutive(struct TreeNode* root) {
    return dfs(root, NULL, 0);
}
