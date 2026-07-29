// LeetCode 0872 - Leaf-Similar Trees
// https://leetcode.com/problems/leaf-similar-trees/

#include <functional>
#include <vector>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right)
        : val(x), left(left), right(right) {}
};

class Solution {
public:
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        auto leaves = [](TreeNode* node) {
            std::vector<int> result;
            std::function<void(TreeNode*)> dfs = [&](TreeNode* cur) {
                if (!cur) {
                    return;
                }
                if (!cur->left && !cur->right) {
                    result.push_back(cur->val);
                    return;
                }
                dfs(cur->left);
                dfs(cur->right);
            };
            dfs(node);
            return result;
        };
        return leaves(root1) == leaves(root2);
    }
};
