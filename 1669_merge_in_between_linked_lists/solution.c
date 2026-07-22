// LeetCode 1669 - Merge In Between Linked Lists
// https://leetcode.com/problems/merge-in-between-linked-lists/

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* mergeInBetween(struct ListNode* list1, int a, int b, struct ListNode* list2) {
    struct ListNode* pre = list1;
    for (int i = 0; i < a - 1; i++) pre = pre->next;
    struct ListNode* post = pre;
    for (int i = 0; i < b - a + 2; i++) post = post->next;
    pre->next = list2;
    while (pre->next) pre = pre->next;
    pre->next = post;
    return list1;
}
