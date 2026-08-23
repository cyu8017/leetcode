// LeetCode 3902 - Zigzag Level Sum Of Binary Tree
// https://leetcode.com/problems/zigzag-level-sum-of-binary-tree/

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
    std::vector<long long> zigzagLevelSum(TreeNode* root) {
        std::vector<long long> ans;
        std::vector<TreeNode*> q = {root};
        bool left = true;
        while (!q.empty()) {
            std::vector<TreeNode*> nq;
            for (TreeNode* node : q) {
                if (node->left) nq.push_back(node->left);
                if (node->right) nq.push_back(node->right);
            }
            int m = (int)q.size();
            long long s = 0;
            for (int i = 0; i < m; i++) {
                TreeNode* node = left ? q[i] : q[m - i - 1];
                TreeNode* child = left ? node->left : node->right;
                if (!child) break;
                s += node->val;
            }
            ans.push_back(s);
            left = !left;
            q.swap(nq);
        }
        return ans;
    }
};
