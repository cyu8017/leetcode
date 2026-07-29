// LeetCode 1474 - Delete N Nodes After M Nodes of a Linked List
// https://leetcode.com/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/

struct ListNode { int val; struct ListNode *next; };

struct ListNode* deleteNodes(struct ListNode* head, int m, int n) {
    struct ListNode* cur = head;
    while (cur) {
        for (int i = 0; i < m - 1 && cur; i++) cur = cur->next;
        if (!cur) break;
        struct ListNode* drop = cur->next;
        for (int i = 0; i < n && drop; i++) drop = drop->next;
        cur->next = drop;
        cur = drop;
    }
    return head;
}
