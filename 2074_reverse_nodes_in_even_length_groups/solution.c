// LeetCode 2074 - Reverse Nodes in Even Length Groups
// https://leetcode.com/problems/reverse-nodes-in-even-length-groups/

#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode* next;
};

struct ListNode* reverseEvenLengthGroups(struct ListNode* head) {
    struct ListNode dummy;
    dummy.next = head;
    struct ListNode* prev = &dummy;
    int group = 1;
    while (prev->next) {
        struct ListNode* cur = prev->next;
        int cnt = 0;
        struct ListNode* node = cur;
        while (node && cnt < group) { node = node->next; cnt++; }
        if (cnt % 2 == 0) {
            struct ListNode* revPrev = node;
            struct ListNode* p = cur;
            for (int i = 0; i < cnt; i++) {
                struct ListNode* nxt = p->next;
                p->next = revPrev;
                revPrev = p;
                p = nxt;
            }
            prev->next = revPrev;
            prev = cur;
        } else {
            for (int i = 0; i < cnt; i++) prev = prev->next;
        }
        group++;
    }
    return dummy.next;
}
