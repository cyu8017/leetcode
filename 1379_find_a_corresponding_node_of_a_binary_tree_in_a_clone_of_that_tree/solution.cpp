struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

#include <vector>
#include <utility>

class Solution {
public:
    TreeNode* getTargetCopy(TreeNode* original, TreeNode* cloned, TreeNode* target) {
        std::vector<std::pair<TreeNode*, TreeNode*>> stack{{original, cloned}};
        while (!stack.empty()) {
            auto [a, b] = stack.back(); stack.pop_back();
            if (a == target || a->val == target->val) return b;
            if (a->left) stack.push_back({a->left, b->left});
            if (a->right) stack.push_back({a->right, b->right});
        }
        return nullptr;
    }
};
