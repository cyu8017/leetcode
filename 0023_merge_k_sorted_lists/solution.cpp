// LeetCode 0023 - Merge k Sorted Lists
// https://leetcode.com/problems/merge-k-sorted-lists/

#include <queue>
#include <vector>

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* mergeKLists(std::vector<ListNode*>& lists) {
        auto cmp = [](ListNode* a, ListNode* b) { return a->val > b->val; };
        std::priority_queue<ListNode*, std::vector<ListNode*>, decltype(cmp)> heap(cmp);

        for (ListNode* node : lists) {
            if (node) {
                heap.push(node);
            }
        }

        ListNode dummy;
        ListNode* current = &dummy;

        while (!heap.empty()) {
            ListNode* node = heap.top();
            heap.pop();
            current->next = node;
            current = current->next;
            if (node->next) {
                heap.push(node->next);
            }
        }

        return dummy.next;
    }
};
