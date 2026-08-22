// LeetCode 0024 - Swap Nodes in Pairs
// https://leetcode.com/problems/swap-nodes-in-pairs/

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* swapPairs(struct ListNode* head) {
    struct ListNode dummy = {0, head};
    struct ListNode* previous = &dummy;

    while (previous->next && previous->next->next) {
        struct ListNode* first = previous->next;
        struct ListNode* second = previous->next->next;
        first->next = second->next;
        second->next = first;
        previous->next = second;
        previous = first;
    }

    return dummy.next;
}
