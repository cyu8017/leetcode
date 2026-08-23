// LeetCode 2476 - Closest Nodes Queries in a Binary Search Tree
// https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/

#include <algorithm>
#include <functional>
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
    std::vector<std::vector<int>> closestNodes(TreeNode* root, std::vector<int>& queries) {
        std::vector<int> vals;
        std::function<void(TreeNode*)> inorder = [&](TreeNode* node) {
            if (!node) return;
            inorder(node->left);
            vals.push_back(node->val);
            inorder(node->right);
        };
        inorder(root);
        std::vector<std::vector<int>> ans(queries.size());
        for (int i = 0; i < (int)queries.size(); i++) {
            int q = queries[i];
            auto it = std::lower_bound(vals.begin(), vals.end(), q);
            int j = (int)(it - vals.begin());
            int mx = j < (int)vals.size() ? vals[j] : -1;
            int mn = -1;
            if (j < (int)vals.size() && vals[j] == q) mn = q;
            else if (j > 0) mn = vals[j - 1];
            ans[i] = {mn, mx};
        }
        return ans;
    }
};
