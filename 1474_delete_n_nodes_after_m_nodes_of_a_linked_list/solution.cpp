struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* deleteNodes(ListNode* head, int m, int n) {
        ListNode* cur = head;
        while (cur) {
            for (int i = 0; i < m - 1 && cur; ++i) cur = cur->next;
            if (!cur) break;
            ListNode* drop = cur->next;
            for (int i = 0; i < n && drop; ++i) drop = drop->next;
            cur->next = drop;
            cur = drop;
        }
        return head;
    }
};
