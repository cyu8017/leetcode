// LeetCode 0124 - Binary Tree Maximum Path Sum
// https://leetcode.com/problems/binary-tree-maximum-path-sum/

#include <algorithm>
#include <climits>
class Solution {
    int best;
    int gain(TreeNode* node) {
        if (!node) return 0;
        int left = std::max(0, gain(node->left)), right = std::max(0, gain(node->right));
        best = std::max(best, node->val + left + right);
        return node->val + std::max(left, right);
    }
public:
    int maxPathSum(TreeNode* root) { best = INT_MIN; gain(root); return best; }
};