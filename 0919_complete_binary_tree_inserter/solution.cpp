// LeetCode 0919 - Complete Binary Tree Inserter
// https://leetcode.com/problems/complete-binary-tree-inserter/

#include <queue>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class CBTInserter {
public:
    CBTInserter(TreeNode* root) : root_(root) {
        std::queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            TreeNode* node = q.front();
            q.pop();
            if (node->left) q.push(node->left);
            else {
                parents_.push(node);
                break;
            }
            if (node->right) q.push(node->right);
            else {
                parents_.push(node);
                break;
            }
        }
        while (!q.empty()) {
            parents_.push(q.front());
            q.pop();
        }
    }

    int insert(int val) {
        TreeNode* parent = parents_.front();
        TreeNode* child = new TreeNode(val);
        if (!parent->left) parent->left = child;
        else {
            parent->right = child;
            parents_.pop();
        }
        parents_.push(child);
        return parent->val;
    }

    TreeNode* get_root() {
        return root_;
    }

private:
    TreeNode* root_;
    std::queue<TreeNode*> parents_;
};
