struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

#include <algorithm>
#include <climits>
#include <tuple>

class Solution {
    int ans = 0;
    std::tuple<bool, int, int, int> dfs(TreeNode* node) {
        if (!node) return {true, INT_MAX, INT_MIN, 0};
        auto [a, lx, lh, ls] = dfs(node->left);
        auto [b, rx, rh, rs] = dfs(node->right);
        if (a && b && lh < node->val && node->val < rx) {
            int s = ls + rs + node->val;
            ans = std::max(ans, s);
            return {true, std::min(lx, node->val), std::max(rh, node->val), s};
        }
        return {false, 0, 0, 0};
    }
public:
    int maxSumBST(TreeNode* root) {
        dfs(root);
        return ans;
    }
};
