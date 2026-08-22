// LeetCode 1721 - Swapping Nodes in a Linked List
// https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* swapNodes(struct ListNode* head, int k) {
    struct ListNode* first = head;
    for (int i = 0; i < k - 1; i++) {
        first = first->next;
    }
    struct ListNode* fast = first;
    struct ListNode* second = head;
    while (fast->next) {
        fast = fast->next;
        second = second->next;
    }
    int temp = first->val;
    first->val = second->val;
    second->val = temp;
    return head;
}
