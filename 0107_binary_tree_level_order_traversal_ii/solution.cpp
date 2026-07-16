// LeetCode 0107 - Binary Tree Level Order Traversal II
// https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

#include <algorithm>
#include <queue>
#include <vector>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    std::vector<std::vector<int>> levelOrderBottom(TreeNode* root) {
        std::vector<std::vector<int>> result;
        if (!root) {
            return result;
        }

        std::queue<TreeNode*> queue;
        queue.push(root);
        while (!queue.empty()) {
            int size = static_cast<int>(queue.size());
            std::vector<int> level;
            level.reserve(size);
            for (int i = 0; i < size; ++i) {
                TreeNode* node = queue.front();
                queue.pop();
                level.push_back(node->val);
                if (node->left) {
                    queue.push(node->left);
                }
                if (node->right) {
                    queue.push(node->right);
                }
            }
            result.push_back(level);
        }

        std::reverse(result.begin(), result.end());
        return result;
    }
};
