// LeetCode 1367 - Linked List in Binary Tree
// https://leetcode.com/problems/linked-list-in-binary-tree/

#include <stdbool.h>

struct ListNode { int val; struct ListNode *next; };
struct TreeNode { int val; struct TreeNode *left; struct TreeNode *right; };

static bool match(struct ListNode* a, struct TreeNode* b) {
    if (!a) return true;
    if (!b || a->val != b->val) return false;
    return match(a->next, b->left) || match(a->next, b->right);
}

bool isSubPath(struct ListNode* head, struct TreeNode* root) {
    if (!root) return false;
    return match(head, root) || isSubPath(head, root->left) || isSubPath(head, root->right);
}
