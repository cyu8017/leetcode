// LeetCode 2058 - Find the Minimum and Maximum Number of Nodes Between Critical Points
// https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/

#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode* next;
};

int* nodesBetweenCriticalPoints(struct ListNode* head, int* returnSize) {
    int crit[100001];
    int cn = 0;
    struct ListNode* prev = head;
    struct ListNode* cur = head->next;
    int idx = 1;
    while (cur && cur->next) {
        if ((cur->val > prev->val && cur->val > cur->next->val) ||
            (cur->val < prev->val && cur->val < cur->next->val)) {
            crit[cn++] = idx;
        }
        prev = cur;
        cur = cur->next;
        idx++;
    }
    int* ans = (int*)malloc(2 * sizeof(int));
    *returnSize = 2;
    if (cn < 2) { ans[0] = -1; ans[1] = -1; return ans; }
    int mn = crit[1] - crit[0];
    for (int i = 2; i < cn; i++) if (crit[i] - crit[i - 1] < mn) mn = crit[i] - crit[i - 1];
    ans[0] = mn;
    ans[1] = crit[cn - 1] - crit[0];
    return ans;
}
