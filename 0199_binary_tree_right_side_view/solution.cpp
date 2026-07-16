// LeetCode 0199 - Binary Tree Right Side View
// https://leetcode.com/problems/binary-tree-right-side-view/

#include <queue>
#include <vector>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
};

class Solution {
public:
    std::vector<int> rightSideView(TreeNode* root) {
        std::vector<int> result;
        if (!root) {
            return result;
        }

        std::queue<TreeNode*> nodes;
        nodes.push(root);
        while (!nodes.empty()) {
            const int level_size = static_cast<int>(nodes.size());
            for (int i = 0; i < level_size; ++i) {
                TreeNode* node = nodes.front();
                nodes.pop();
                if (i == level_size - 1) {
                    result.push_back(node->val);
                }
                if (node->left) nodes.push(node->left);
                if (node->right) nodes.push(node->right);
            }
        }
        return result;
    }
};
