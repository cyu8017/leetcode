// LeetCode 0230 - Kth Smallest Element in a BST
// https://leetcode.com/problems/kth-smallest-element-in-a-bst/

#include <stack>
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
    int kthSmallest(TreeNode* root, int k) {
        std::stack<TreeNode*> nodes;
        TreeNode* current = root;

        while (current || !nodes.empty()) {
            while (current) {
                nodes.push(current);
                current = current->left;
            }
            current = nodes.top();
            nodes.pop();
            k--;
            if (k == 0) {
                return current->val;
            }
            current = current->right;
        }

        return -1;
    }
};
