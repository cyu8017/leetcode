// LeetCode 0086 - Partition List
// https://leetcode.com/problems/partition-list/

#include <stddef.h>

struct ListNode {
    int val;
    struct ListNode* next;
};

struct ListNode* partition(struct ListNode* head, int x) {
    struct ListNode beforeHead;
    struct ListNode afterHead;
    beforeHead.next = NULL;
    afterHead.next = NULL;
    struct ListNode* before = &beforeHead;
    struct ListNode* after = &afterHead;

    while (head) {
        if (head->val < x) {
            before->next = head;
            before = before->next;
        } else {
            after->next = head;
            after = after->next;
        }
        head = head->next;
    }

    after->next = NULL;
    before->next = afterHead.next;
    return beforeHead.next;
}
