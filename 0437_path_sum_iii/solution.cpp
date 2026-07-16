// LeetCode 0437 - Path Sum III
// https://leetcode.com/problems/path-sum-iii/

#include <unordered_map>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
    int dfs(TreeNode* node, long long current, int targetSum, std::unordered_map<long long, int>& prefixCounts) {
        if (node == nullptr) {
            return 0;
        }

        current += node->val;
        int total = prefixCounts[current - targetSum];
        ++prefixCounts[current];

        total += dfs(node->left, current, targetSum, prefixCounts);
        total += dfs(node->right, current, targetSum, prefixCounts);

        --prefixCounts[current];
        return total;
    }

public:
    int pathSum(TreeNode* root, int targetSum) {
        std::unordered_map<long long, int> prefixCounts;
        prefixCounts[0] = 1;
        return dfs(root, 0, targetSum, prefixCounts);
    }
};
