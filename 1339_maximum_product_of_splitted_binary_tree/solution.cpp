#include <algorithm>
#include <vector>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
    std::vector<long long> sums;
    long long total(TreeNode* node) {
        if (!node) return 0;
        long long value = node->val + total(node->left) + total(node->right);
        sums.push_back(value);
        return value;
    }
public:
    int maxProduct(TreeNode* root) {
        long long whole = total(root);
        long long best = 0;
        for (long long value : sums) best = std::max(best, value * (whole - value));
        return (int)(best % 1000000007);
    }
};
