// LeetCode 3217 - Delete Nodes From Linked List Present in Array
// https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

struct ListNode {
    int val;
    struct ListNode* next;
};

enum { H3217 = 200003 };
typedef struct { int key; int used; } E3217;

struct ListNode* modifiedList(int* nums, int numsSize, struct ListNode* head) {
    E3217* s = calloc(H3217, sizeof(E3217));
    for (int i = 0; i < numsSize; i++) {
        unsigned h = ((unsigned)nums[i] * 2654435761u) % H3217;
        while (s[h].used && s[h].key != nums[i]) h = (h + 1) % H3217;
        s[h].used = 1; s[h].key = nums[i];
    }
    struct ListNode dummy = {0, head};
    for (struct ListNode* pre = &dummy; pre->next; ) {
        int v = pre->next->val;
        unsigned h = ((unsigned)v * 2654435761u) % H3217;
        int found = 0;
        while (s[h].used) {
            if (s[h].key == v) { found = 1; break; }
            h = (h + 1) % H3217;
        }
        if (found) pre->next = pre->next->next;
        else pre = pre->next;
    }
    free(s);
    return dummy.next;
}
