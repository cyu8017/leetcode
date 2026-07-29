// LeetCode 1973 - Count Nodes Equal to Sum of Descendants
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
    int equalToDescendants(TreeNode* root) {
        int ans = 0;
        std::function<long long(TreeNode*)> dfs = [&](TreeNode* node) -> long long {
            if (!node) return 0;
            long long total = dfs(node->left) + dfs(node->right);
            if (total == node->val) ans++;
            return total + node->val;
        };
        dfs(root);
        return ans;
    }
};
