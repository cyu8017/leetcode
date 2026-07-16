// LeetCode 0142 - Linked List Cycle II
// https://leetcode.com/problems/linked-list-cycle-ii/

#include <stddef.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode *detectCycle(struct ListNode *head) {
    struct ListNode *slow = head;
    struct ListNode *fast = head;

    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) {
            slow = head;
            while (slow != fast) {
                slow = slow->next;
                fast = fast->next;
            }
            return slow;
        }
    }
    return NULL;
}
// LeetCode 0142 - Linked List Cycle II
// https://leetcode.com/problems/linked-list-cycle-ii/

void solve() {
}