// LeetCode 0203 - Remove Linked List Elements
struct ListNode { int val; struct ListNode *next; };
struct ListNode* removeElements(struct ListNode* head, int val) {
    struct ListNode dummy = {0, head}; struct ListNode* current = &dummy;
    while (current->next) { if (current->next->val == val) current->next = current->next->next; else current = current->next; }
    return dummy.next;
}
