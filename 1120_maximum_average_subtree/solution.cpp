// LeetCode 1120 - Maximum Average Subtree
// https://leetcode.com/problems/maximum-average-subtree/

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
public:
    double maximumAverageSubtree(TreeNode* root) {
        best = 0.0;
        dfs(root);
        return best;
    }

private:
    double best = 0.0;

    std::pair<int, int> dfs(TreeNode* node) {
        if (!node) {
            return {0, 0};
        }
        auto [leftSum, leftCount] = dfs(node->left);
        auto [rightSum, rightCount] = dfs(node->right);
        int totalSum = leftSum + rightSum + node->val;
        int totalCount = leftCount + rightCount + 1;
        best = std::max(best, static_cast<double>(totalSum) / totalCount);
        return {totalSum, totalCount};
    }
};
