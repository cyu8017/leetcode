// LeetCode 0023 - Merge k Sorted Lists
// https://leetcode.com/problems/merge-k-sorted-lists/

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* mergeKLists(struct ListNode** lists, int listsSize) {
    struct ListNode dummy = {0, NULL};
    struct ListNode* current = &dummy;

    while (1) {
        int minIdx = -1;
        int minVal = 0;

        for (int i = 0; i < listsSize; i++) {
            if (lists[i]) {
                if (minIdx == -1 || lists[i]->val < minVal) {
                    minIdx = i;
                    minVal = lists[i]->val;
                }
            }
        }

        if (minIdx == -1) {
            break;
        }

        current->next = lists[minIdx];
        current = lists[minIdx];
        lists[minIdx] = lists[minIdx]->next;
    }

    return dummy.next;
}
