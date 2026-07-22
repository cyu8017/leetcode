// LeetCode 1602 - Find Nearest Right Node in Binary Tree
// https://leetcode.com/problems/find-nearest-right-node-in-binary-tree/

#include <queue>

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
    TreeNode* findNearestRightNode(TreeNode* root, int u) {
        if (!root) {
            return nullptr;
        }
        std::queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            const int size = static_cast<int>(q.size());
            for (int i = 0; i < size; ++i) {
                TreeNode* node = q.front();
                q.pop();
                if (node->val == u) {
                    return (i + 1 < size) ? q.front() : nullptr;
                }
                if (node->left) {
                    q.push(node->left);
                }
                if (node->right) {
                    q.push(node->right);
                }
            }
        }
        return nullptr;
    }
};
