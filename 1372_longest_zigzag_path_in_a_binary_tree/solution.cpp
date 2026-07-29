struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

#include <algorithm>
#include <utility>

class Solution {
    int ans = 0;
    std::pair<int, int> dfs(TreeNode* node) {
        if (!node) return {-1, -1};
        auto l = dfs(node->left), r = dfs(node->right);
        int a = l.second + 1, b = r.first + 1;
        ans = std::max({ans, a, b});
        return {a, b};
    }
public:
    int longestZigZag(TreeNode* root) {
        dfs(root);
        return ans;
    }
};
