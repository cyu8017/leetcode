// LeetCode 1171 - Remove Zero Sum Consecutive Nodes from Linked List
// https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/

#include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode* next;
};

struct ListNode* removeZeroSumSublists(struct ListNode* head) {
    struct ListNode dummy;
    dummy.val = 0;
    dummy.next = head;
    // Two-pass map via arrays (prefix -> last node)
    struct ListNode* nodes[2005];
    int prefixes[2005];
    int count = 0;
    int prefix = 0;
    struct ListNode* node = &dummy;
    while (node) {
        prefix += node->val;
        // overwrite existing same prefix
        int found = -1;
        for (int i = 0; i < count; i++) if (prefixes[i] == prefix) { found = i; break; }
        if (found >= 0) {
            nodes[found] = node;
            count = found + 1;
        } else {
            prefixes[count] = prefix;
            nodes[count] = node;
            count++;
        }
        node = node->next;
    }
    // rebuild: second pass matching python
    // Build map prefix->node from first full scan then rewire
    // Re-do like python exactly:
    struct ListNode* mapNodes[2005];
    int mapPref[2005];
    int mapN = 0;
    prefix = 0;
    node = &dummy;
    while (node) {
        prefix += node->val;
        int found = -1;
        for (int i = 0; i < mapN; i++) if (mapPref[i] == prefix) { found = i; break; }
        if (found >= 0) mapNodes[found] = node;
        else { mapPref[mapN] = prefix; mapNodes[mapN] = node; mapN++; }
        node = node->next;
    }
    prefix = 0;
    node = &dummy;
    while (node) {
        prefix += node->val;
        for (int i = 0; i < mapN; i++) {
            if (mapPref[i] == prefix) {
                node->next = mapNodes[i]->next;
                break;
            }
        }
        node = node->next;
    }
    return dummy.next;
}
