// LeetCode 1290 - Convert Binary Number in a Linked List to Integer
// https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

struct ListNode {
    int val;
    struct ListNode* next;
};

int getDecimalValue(struct ListNode* head) {
    int value = 0;
    while (head) {
        value = value * 2 + head->val;
        head = head->next;
    }
    return value;
}
