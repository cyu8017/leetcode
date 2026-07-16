// LeetCode 0061 - Rotate List
// https://leetcode.com/problems/rotate-list/

struct ListNode {
    int val;
    struct ListNode* next;
};

struct ListNode* rotateRight(struct ListNode* head, int k) {
    if (!head || !head->next) {
        return head;
    }

    struct ListNode* tail = head;
    int length = 1;
    while (tail->next) {
        tail = tail->next;
        length++;
    }

    tail->next = head;
    k %= length;
    if (k == 0) {
        tail->next = NULL;
        return head;
    }

    int steps = length - k;
    struct ListNode* new_tail = head;
    for (int i = 0; i < steps - 1; i++) {
        new_tail = new_tail->next;
    }

    struct ListNode* new_head = new_tail->next;
    new_tail->next = NULL;
    return new_head;
}
