// LeetCode 0147 - Insertion Sort List
// https://leetcode.com/problems/insertion-sort-list/

#include <stddef.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode *insertionSortList(struct ListNode *head) {
    struct ListNode dummy = {0, NULL};
    while (head) {
        struct ListNode *next = head->next;
        struct ListNode *previous = &dummy;
        while (previous->next && previous->next->val < head->val) {
            previous = previous->next;
        }
        head->next = previous->next;
        previous->next = head;
        head = next;
    }
    return dummy.next;
}
// LeetCode 0147 - Insertion Sort List
// https://leetcode.com/problems/insertion-sort-list/

void solve() {
}