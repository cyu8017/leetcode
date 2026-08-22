// LeetCode 0025 - Reverse Nodes in k-Group
// https://leetcode.com/problems/reverse-nodes-in-k-group/

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* reverseKGroup(struct ListNode* head, int k) {
    struct ListNode dummy = {0, head};
    struct ListNode* groupPrevious = &dummy;

    while (1) {
        struct ListNode* kth = groupPrevious;
        for (int i = 0; i < k; i++) {
            kth = kth->next;
            if (!kth) {
                return dummy.next;
            }
        }

        struct ListNode* groupNext = kth->next;
        struct ListNode* previous = groupNext;
        struct ListNode* current = groupPrevious->next;

        while (current != groupNext) {
            struct ListNode* next = current->next;
            current->next = previous;
            previous = current;
            current = next;
        }

        struct ListNode* tmp = groupPrevious->next;
        groupPrevious->next = kth;
        groupPrevious = tmp;
    }
}
