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
    void inorder(TreeNode* root, std::vector<int>& out) {
        if (!root) return;
        inorder(root->left, out);
        out.push_back(root->val);
        inorder(root->right, out);
    }
public:
    std::vector<int> getAllElements(TreeNode* root1, TreeNode* root2) {
        std::vector<int> a, b, answer;
        inorder(root1, a);
        inorder(root2, b);
        size_t i = 0, j = 0;
        while (i < a.size() || j < b.size()) {
            if (j == b.size() || (i < a.size() && a[i] <= b[j])) answer.push_back(a[i++]);
            else answer.push_back(b[j++]);
        }
        return answer;
    }
};
