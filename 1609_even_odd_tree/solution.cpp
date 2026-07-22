// LeetCode 1609 - Even Odd Tree
// https://leetcode.com/problems/even-odd-tree/

#include <climits>
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
    bool isEvenOddTree(TreeNode* root) {
        if (!root) {
            return true;
        }
        std::queue<TreeNode*> q;
        q.push(root);
        int level = 0;
        while (!q.empty()) {
            const int size = static_cast<int>(q.size());
            int prev = (level % 2 == 0) ? INT_MIN : INT_MAX;
            for (int i = 0; i < size; ++i) {
                TreeNode* node = q.front();
                q.pop();
                if (node->val % 2 == level % 2) {
                    return false;
                }
                if (level % 2 == 0 && node->val <= prev) {
                    return false;
                }
                if (level % 2 == 1 && node->val >= prev) {
                    return false;
                }
                prev = node->val;
                if (node->left) {
                    q.push(node->left);
                }
                if (node->right) {
                    q.push(node->right);
                }
            }
            ++level;
        }
        return true;
    }
};
