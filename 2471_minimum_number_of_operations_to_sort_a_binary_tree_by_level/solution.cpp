// LeetCode 2471 - Minimum Number of Operations to Sort a Binary Tree by Level
// https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/

#include <algorithm>
#include <queue>
#include <unordered_map>
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
    int minimumOperations(TreeNode* root) {
        if (!root) return 0;
        int ans = 0;
        std::queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            int sz = (int)q.size();
            std::vector<int> vals(sz);
            for (int i = 0; i < sz; i++) {
                TreeNode* node = q.front();
                q.pop();
                vals[i] = node->val;
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            std::vector<int> sorted = vals;
            std::sort(sorted.begin(), sorted.end());
            std::unordered_map<int, int> pos;
            for (int i = 0; i < sz; i++) pos[vals[i]] = i;
            for (int i = 0; i < sz; i++) {
                if (vals[i] != sorted[i]) {
                    int j = pos[sorted[i]];
                    std::swap(vals[i], vals[j]);
                    pos[vals[j]] = j;
                    pos[vals[i]] = i;
                    ans++;
                }
            }
        }
        return ans;
    }
};
