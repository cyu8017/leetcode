// LeetCode 0206 - Reverse Linked List
struct ListNode { int val; struct ListNode *next; };
struct ListNode* reverseList(struct ListNode* head) { struct ListNode* previous = 0; while (head) { struct ListNode* next = head->next; head->next = previous; previous = head; head = next; } return previous; }
