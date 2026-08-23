// LeetCode 0513 - Find Bottom Left Tree Value
// https://leetcode.com/problems/find-bottom-left-tree-value/

#include <queue>
#include <vector>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    int findBottomLeftValue(TreeNode* root) {
        std::queue<TreeNode*> queue;
        queue.push(root);
        int leftmost = root->val;
        while (!queue.empty()) {
            const int levelSize = static_cast<int>(queue.size());
            for (int index = 0; index < levelSize; ++index) {
                TreeNode* node = queue.front();
                queue.pop();
                if (index == 0) {
                    leftmost = node->val;
                }
                if (node->left) {
                    queue.push(node->left);
                }
                if (node->right) {
                    queue.push(node->right);
                }
            }
        }
        return leftmost;
    }
};
