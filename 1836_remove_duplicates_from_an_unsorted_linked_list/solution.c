// LeetCode 1836 - Remove Duplicates From an Unsorted Linked List
// https://leetcode.com/problems/remove-duplicates-from-an-unsorted-linked-list/

#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode* next;
};

struct ListNode* deleteDuplicatesUnsorted(struct ListNode* head) {
    int counts[100001] = {0};
    for (struct ListNode* node = head; node; node = node->next) {
        counts[node->val]++;
    }

    struct ListNode dummy;
    dummy.val = 0;
    dummy.next = head;
    struct ListNode* prev = &dummy;
    struct ListNode* node = head;
    while (node) {
        if (counts[node->val] > 1) {
            prev->next = node->next;
            node = node->next;
        } else {
            prev = node;
            node = node->next;
        }
    }
    return dummy.next;
}
