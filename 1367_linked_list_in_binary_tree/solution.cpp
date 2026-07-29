struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
    bool match(ListNode* a, TreeNode* b) {
        if (!a) return true;
        if (!b || a->val != b->val) return false;
        return match(a->next, b->left) || match(a->next, b->right);
    }
public:
    bool isSubPath(ListNode* head, TreeNode* root) {
        if (!root) return false;
        return match(head, root) || isSubPath(head, root->left) || isSubPath(head, root->right);
    }
};
