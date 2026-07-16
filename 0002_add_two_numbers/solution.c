// LeetCode 0002 - Add Two Numbers
// https://leetcode.com/problems/add-two-numbers/

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode dummy = {0, NULL};
    struct ListNode* current = &dummy;
    int carry = 0;

    while (l1 || l2 || carry) {
        int total = carry;
        if (l1) {
            total += l1->val;
            l1 = l1->next;
        }
        if (l2) {
            total += l2->val;
            l2 = l2->next;
        }
        carry = total / 10;
        struct ListNode* node = (struct ListNode*)malloc(sizeof(struct ListNode));
        node->val = total % 10;
        node->next = NULL;
        current->next = node;
        current = node;
    }

    return dummy.next;
}
