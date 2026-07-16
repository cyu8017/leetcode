// LeetCode 0366 - Find Leaves of Binary Tree
// https://leetcode.com/problems/find-leaves-of-binary-tree/

#include <algorithm>
#include <vector>

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
    std::vector<std::vector<int>> findLeaves(TreeNode* root) {
        std::vector<std::vector<int>> layers;
        dfs(root, layers);
        return layers;
    }

private:
    int dfs(TreeNode* node, std::vector<std::vector<int>>& layers) {
        if (node == nullptr) {
            return -1;
        }

        int height = std::max(dfs(node->left, layers), dfs(node->right, layers)) + 1;
        if (static_cast<int>(layers.size()) <= height) {
            layers.resize(height + 1);
        }
        layers[height].push_back(node->val);
        return height;
    }
};
