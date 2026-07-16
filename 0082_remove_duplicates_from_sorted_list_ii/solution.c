// LeetCode 0082 - Remove Duplicates from Sorted List II
// https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* deleteDuplicates(struct ListNode* head) {
    struct ListNode dummy = {0, head};
    struct ListNode* previous = &dummy;

    while (head) {
        if (head->next && head->val == head->next->val) {
            while (head->next && head->val == head->next->val) {
                head = head->next;
            }
            previous->next = head->next;
        } else {
            previous = previous->next;
        }
        head = head->next;
    }

    return dummy.next;
}
