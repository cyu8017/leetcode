// LeetCode 2689 - Extract Kth Character From The Rope Tree
// https://leetcode.com/problems/extract-kth-character-from-the-rope-tree/

struct RopeTreeNode {
    int len;
    char val;
    RopeTreeNode* left;
    RopeTreeNode* right;
    RopeTreeNode() : len(0), val(0), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    char getKthCharacter(RopeTreeNode* root, int k) {
        auto dfs = [&](auto&& self, RopeTreeNode* node, int kk) -> char {
            if (!node->left && !node->right) return node->val;
            int leftLen = 0;
            if (node->left) leftLen = node->left->len > 0 ? node->left->len : 1;
            if (kk <= leftLen) return self(self, node->left, kk);
            return self(self, node->right, kk - leftLen);
        };
        return dfs(dfs, root, k);
    }
};
