// LeetCode 3062 - Winner of the Linked List Game
// https://leetcode.com/problems/winner-of-the-linked-list-game/

#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode* next;
};

char* gameResult(struct ListNode* head) {
    int odd = 0, even = 0;
    while (head) {
        int a = head->val, b = head->next->val;
        if (a < b) odd++;
        if (a > b) even++;
        head = head->next->next;
    }
    if (odd > even) return "Odd";
    if (odd < even) return "Even";
    return "Tie";
}
