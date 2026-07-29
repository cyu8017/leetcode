// LeetCode 1161 - Maximum Level Sum of a Binary Tree
// https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

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
    int maxLevelSum(TreeNode* root) {
        std::queue<TreeNode*> q;
        q.push(root);
        int bestSum = INT_MIN, bestLevel = 1, level = 1;
        while (!q.empty()) {
            int total = 0, sz = static_cast<int>(q.size());
            for (int i = 0; i < sz; ++i) {
                TreeNode* node = q.front(); q.pop();
                total += node->val;
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            if (total > bestSum) { bestSum = total; bestLevel = level; }
            ++level;
        }
        return bestLevel;
    }
};
