// LeetCode 1669 - Merge In Between Linked Lists
// https://leetcode.com/problems/merge-in-between-linked-lists/

struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        ListNode* pre = list1;
        for (int i = 0; i < a - 1; ++i) {
            pre = pre->next;
        }
        ListNode* post = pre;
        for (int i = 0; i < b - a + 2; ++i) {
            post = post->next;
        }
        pre->next = list2;
        while (pre->next) {
            pre = pre->next;
        }
        pre->next = post;
        return list1;
    }
};
