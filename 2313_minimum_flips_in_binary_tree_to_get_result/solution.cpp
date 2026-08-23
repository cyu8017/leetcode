// LeetCode 2313 - Minimum Flips in Binary Tree to Get Result
// https://leetcode.com/problems/minimum-flips-in-binary-tree-to-get-result/

#include <utility>
#include <algorithm>
#include <functional>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    int minimumFlips(TreeNode* root, bool result) {
        std::function<std::pair<int,int>(TreeNode*)> dfs = [&](TreeNode* node) -> std::pair<int,int> {
            if (!node->left && !node->right)
                return node->val == 0 ? std::pair{0, 1} : std::pair{1, 0};
            if (node->val == 5) {
                auto [f, t] = dfs(node->left);
                return {t, f};
            }
            auto [lf, lt] = dfs(node->left);
            auto [rf, rt] = dfs(node->right);
            if (node->val == 2) return {lf + rf, std::min({lt + rt, lt + rf, lf + rt})};
            if (node->val == 3) return {std::min({lf + rf, lf + rt, lt + rf}), lt + rt};
            if (node->val == 4) return {std::min(lf + rf, lt + rt), std::min(lf + rt, lt + rf)};
            return {0, 0};
        };
        auto [f, t] = dfs(root);
        return result ? t : f;
    }
};
