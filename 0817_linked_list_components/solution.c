// LeetCode 0817 - Linked List Components
// https://leetcode.com/problems/linked-list-components/

#include <stdbool.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

int numComponents(struct ListNode* head, int* nums, int numsSize) {
    bool present[10001] = {0};
    for (int i = 0; i < numsSize; i++) present[nums[i]] = true;
    int count = 0;
    bool connected = false;
    while (head) {
        if (present[head->val]) {
            if (!connected) { count++; connected = true; }
        } else connected = false;
        head = head->next;
    }
    return count;
}
