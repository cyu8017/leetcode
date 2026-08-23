// LeetCode 3157 - Find the Level of Tree with Minimum Sum
// https://leetcode.com/problems/find-the-level-of-tree-with-minimum-sum/

#include <queue>
#include <climits>

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
    int minimumLevel(TreeNode* root) {
        std::queue<TreeNode*> q;
        q.push(root);
        long long s = LLONG_MAX;
        int ans = 0;
        for (int level = 1; !q.empty(); level++) {
            long long t = 0;
            int m = (int)q.size();
            while (m--) {
                TreeNode* node = q.front(); q.pop();
                t += node->val;
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            if (s > t) { s = t; ans = level; }
        }
        return ans;
    }
};
