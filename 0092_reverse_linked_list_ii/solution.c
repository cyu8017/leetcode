// LeetCode 0092 - Reverse Linked List II
// https://leetcode.com/problems/reverse-linked-list-ii/

struct ListNode {
    int val;
    struct ListNode* next;
};

struct ListNode* reverseBetween(struct ListNode* head, int left, int right) {
    if (!head || left == right) {
        return head;
    }

    struct ListNode dummy;
    dummy.val = 0;
    dummy.next = head;

    struct ListNode* before = &dummy;
    for (int i = 0; i < left - 1; i++) {
        before = before->next;
    }

    struct ListNode* start = before->next;
    struct ListNode* current = start->next;

    for (int i = 0; i < right - left; i++) {
        start->next = current->next;
        current->next = before->next;
        before->next = current;
        current = start->next;
    }

    return dummy.next;
}
