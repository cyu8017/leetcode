// LeetCode 0337 - House Robber III
// https://leetcode.com/problems/house-robber-iii/

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
    int rob(TreeNode* root) {
        auto [withRob, withoutRob] = dfs(root);
        return std::max(withRob, withoutRob);
    }

private:
    std::pair<int, int> dfs(TreeNode* node) {
        if (node == nullptr) {
            return {0, 0};
        }

        auto [leftWith, leftWithout] = dfs(node->left);
        auto [rightWith, rightWithout] = dfs(node->right);

        int withRob = node->val + leftWithout + rightWithout;
        int withoutRob = std::max(leftWith, leftWithout) + std::max(rightWith, rightWithout);
        return {withRob, withoutRob};
    }
};
