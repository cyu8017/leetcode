// LeetCode 0083 - Remove Duplicates from Sorted List
// https://leetcode.com/problems/remove-duplicates-from-sorted-list/

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* deleteDuplicates(struct ListNode* head) {
    struct ListNode* current = head;

    while (current && current->next) {
        if (current->val == current->next->val) {
            current->next = current->next->next;
        } else {
            current = current->next;
        }
    }

    return head;
}
