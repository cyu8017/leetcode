// LeetCode 1145 - Binary Tree Coloring Game
// https://leetcode.com/problems/binary-tree-coloring-game/

#include <algorithm>

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
    bool btreeGameWinningMove(TreeNode* root, int n, int x) {
        leftCount = rightCount = 0;
        dfs(root, x);
        return std::max({leftCount, rightCount, n - leftCount - rightCount - 1}) > n / 2;
    }

private:
    int leftCount = 0, rightCount = 0;
    int dfs(TreeNode* node, int x) {
        if (!node) return 0;
        int l = dfs(node->left, x), r = dfs(node->right, x);
        if (node->val == x) { leftCount = l; rightCount = r; }
        return l + r + 1;
    }
};
