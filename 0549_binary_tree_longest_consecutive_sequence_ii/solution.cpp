// LeetCode 0549 - Binary Tree Longest Consecutive Sequence II
// https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/

#include <algorithm>
#include <utility>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
};

class Solution {
    int best_ = 0;

    std::pair<int, int> dfs(TreeNode* node) {
        if (!node) {
            return {0, 0};
        }

        const auto [leftInc, leftDec] = dfs(node->left);
        const auto [rightInc, rightDec] = dfs(node->right);

        int inc = 1;
        int dec = 1;
        if (node->left) {
            if (node->left->val == node->val + 1) {
                inc = std::max(inc, leftInc + 1);
            } else if (node->left->val == node->val - 1) {
                dec = std::max(dec, leftDec + 1);
            }
        }
        if (node->right) {
            if (node->right->val == node->val + 1) {
                inc = std::max(inc, rightInc + 1);
            } else if (node->right->val == node->val - 1) {
                dec = std::max(dec, rightDec + 1);
            }
        }

        if (node->left && node->right) {
            if (node->left->val + 1 == node->val && node->val + 1 == node->right->val) {
                best_ = std::max(best_, leftDec + 1 + rightInc);
            }
            if (node->left->val - 1 == node->val && node->val - 1 == node->right->val) {
                best_ = std::max(best_, leftInc + 1 + rightDec);
            }
        }

        best_ = std::max({best_, inc, dec});
        return {inc, dec};
    }

public:
    int longestConsecutive(TreeNode* root) {
        best_ = 0;
        dfs(root);
        return best_;
    }
};
