// LeetCode 0988 - Smallest String Starting From Leaf
// https://leetcode.com/problems/smallest-string-starting-from-leaf/

#include <string>

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
    std::string smallestFromLeaf(TreeNode* root) {
        std::string best = "~";
        auto dfs = [&](auto&& self, TreeNode* node, std::string path) -> void {
            if (!node) return;
            path = char('a' + node->val) + path;
            if (!node->left && !node->right) {
                if (path < best) best = path;
                return;
            }
            self(self, node->left, path);
            self(self, node->right, path);
        };
        dfs(dfs, root, "");
        return best;
    }
};
