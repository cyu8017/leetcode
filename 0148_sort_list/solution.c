// LeetCode 0148 - Sort List
// https://leetcode.com/problems/sort-list/

#include <stddef.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

static struct ListNode *merge(struct ListNode *left, struct ListNode *right) {
    struct ListNode dummy = {0, NULL};
    struct ListNode *tail = &dummy;
    while (left && right) {
        if (left->val <= right->val) {
            tail->next = left;
            left = left->next;
        } else {
            tail->next = right;
            right = right->next;
        }
        tail = tail->next;
    }
    tail->next = left ? left : right;
    return dummy.next;
}

struct ListNode *sortList(struct ListNode *head) {
    if (!head || !head->next) return head;
    struct ListNode *slow = head;
    struct ListNode *fast = head->next;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }
    struct ListNode *right = slow->next;
    slow->next = NULL;
    return merge(sortList(head), sortList(right));
}
// LeetCode 0148 - Sort List
// https://leetcode.com/problems/sort-list/

void solve() {
}