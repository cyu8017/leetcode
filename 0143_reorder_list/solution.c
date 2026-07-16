// LeetCode 0143 - Reorder List
// https://leetcode.com/problems/reorder-list/

#include <stddef.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

void reorderList(struct ListNode *head) {
    if (!head || !head->next) {
        return;
    }

    struct ListNode *slow = head;
    struct ListNode *fast = head;
    while (fast->next && fast->next->next) {
        slow = slow->next;
        fast = fast->next->next;
    }

    struct ListNode *second = slow->next;
    slow->next = NULL;
    struct ListNode *previous = NULL;
    while (second) {
        struct ListNode *next = second->next;
        second->next = previous;
        previous = second;
        second = next;
    }

    struct ListNode *first = head;
    second = previous;
    while (second) {
        struct ListNode *first_next = first->next;
        struct ListNode *second_next = second->next;
        first->next = second;
        second->next = first_next;
        first = first_next;
        second = second_next;
    }
}
// LeetCode 0143 - Reorder List
// https://leetcode.com/problems/reorder-list/

void solve() {
}