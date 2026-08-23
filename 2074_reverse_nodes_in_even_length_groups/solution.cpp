// LeetCode 2074 - Reverse Nodes in Even Length Groups
// https://leetcode.com/problems/reverse-nodes-in-even-length-groups/

struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* reverseEvenLengthGroups(ListNode* head) {
        ListNode dummy(0, head);
        ListNode* prev = &dummy;
        int group = 1;
        while (prev->next) {
            ListNode* cur = prev->next;
            int cnt = 0;
            ListNode* node = cur;
            while (node && cnt < group) { node = node->next; cnt++; }
            if (cnt % 2 == 0) {
                ListNode* revPrev = node;
                ListNode* p = cur;
                for (int i = 0; i < cnt; i++) {
                    ListNode* nxt = p->next;
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
};
