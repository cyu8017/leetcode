// LeetCode 0106 - Construct Binary Tree from Inorder and Postorder Traversal
// https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

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
    TreeNode* buildTree(std::vector<int>& inorder, std::vector<int>& postorder) {
        std::unordered_map<int, int> index;
        for (int i = 0; i < (int)inorder.size(); i++) {
            index[inorder[i]] = i;
        }
        int postIndex = (int)postorder.size() - 1;
        return build(postorder, index, postIndex, 0, (int)inorder.size() - 1);
    }

private:
    TreeNode* build(std::vector<int>& postorder, std::unordered_map<int, int>& index,
                    int& postIndex, int left, int right) {
        if (left > right) {
            return nullptr;
        }
        int rootVal = postorder[postIndex--];
        int mid = index[rootVal];
        TreeNode* root = new TreeNode(rootVal);
        root->right = build(postorder, index, postIndex, mid + 1, right);
        root->left = build(postorder, index, postIndex, left, mid - 1);
        return root;
    }
};