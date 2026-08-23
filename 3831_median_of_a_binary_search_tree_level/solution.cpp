// LeetCode 3831 - Median Of A Binary Search Tree Level
// https://leetcode.com/problems/median-of-a-binary-search-tree-level/

#include <functional>
#include <vector>

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
    int levelMedian(TreeNode* root, int level) {
        std::vector<int> nums;
        std::function<void(TreeNode*, int)> dfs = [&](TreeNode* node, int i) {
            if (!node) return;
            dfs(node->left, i + 1);
            if (i == level) nums.push_back(node->val);
            dfs(node->right, i + 1);
        };
        dfs(root, 0);
        if (nums.empty()) return -1;
        return nums[nums.size() / 2];
    }
};
