// LeetCode 0623 - Add One Row to Tree
// https://leetcode.com/problems/add-one-row-to-tree/

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
};

class Solution {
    int val_ = 0;
    int depth_ = 0;

    void dfs(TreeNode* node, int current) {
        if (!node) {
            return;
        }
        if (current == depth_ - 1) {
            node->left = new TreeNode(val_, node->left, nullptr);
            node->right = new TreeNode(val_, nullptr, node->right);
            return;
        }
        dfs(node->left, current + 1);
        dfs(node->right, current + 1);
    }

public:
    TreeNode* addOneRow(TreeNode* root, int val, int depth) {
        if (depth == 1) {
            return new TreeNode(val, root, nullptr);
        }
        val_ = val;
        depth_ = depth;
        dfs(root, 1);
        return root;
    }
};
