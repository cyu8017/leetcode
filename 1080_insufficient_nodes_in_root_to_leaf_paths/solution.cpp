// LeetCode 1080 - Insufficient Nodes in Root to Leaf Paths
// https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    TreeNode* sufficientSubset(TreeNode* root, int limit) {
        return dfs(root, 0, limit);
    }

private:
    TreeNode* dfs(TreeNode* node, int pathSum, int limit) {
        if (!node) {
            return nullptr;
        }
        pathSum += node->val;
        if (!node->left && !node->right) {
            return pathSum >= limit ? node : nullptr;
        }
        node->left = dfs(node->left, pathSum, limit);
        node->right = dfs(node->right, pathSum, limit);
        if (!node->left && !node->right) {
            return nullptr;
        }
        return node;
    }
};
