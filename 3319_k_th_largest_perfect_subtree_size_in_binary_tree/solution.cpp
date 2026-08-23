// LeetCode 3319 - K-th Largest Perfect Subtree Size in Binary Tree
// https://leetcode.com/problems/k-th-largest-perfect-subtree-size-in-binary-tree/

#include <algorithm>
#include <functional>
#include <tuple>
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
public:
    int kthLargestPerfectSubtree(TreeNode* root, int k) {
        std::vector<int> sizes;
        std::function<std::tuple<int, int, bool>(TreeNode*)> dfs = [&](TreeNode* node) -> std::tuple<int, int, bool> {
            if (!node) return {0, 0, true};
            auto [lh, ls, lp] = dfs(node->left);
            auto [rh, rs, rp] = dfs(node->right);
            int sz = ls + rs + 1;
            bool perf = lp && rp && lh == rh;
            if (perf) sizes.push_back(sz);
            return {std::max(lh, rh) + 1, sz, perf};
        };
        dfs(root);
        std::sort(sizes.begin(), sizes.end(), std::greater<int>());
        if (k > (int)sizes.size()) return -1;
        return sizes[k - 1];
    }
};
