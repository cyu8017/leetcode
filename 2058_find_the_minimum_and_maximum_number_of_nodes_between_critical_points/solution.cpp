// LeetCode 2058 - Find the Minimum and Maximum Number of Nodes Between Critical Points
// https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/

#include <algorithm>
#include <array>
#include <bitset>
#include <cmath>
#include <cstdint>
#include <deque>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};

class Solution {
public:
    vector<int> nodesBetweenCriticalPoints(ListNode* head) {
        vector<int> crit;
        ListNode* prev = head;
        ListNode* cur = head->next;
        int idx = 1;
        while (cur && cur->next) {
            if ((cur->val > prev->val && cur->val > cur->next->val) ||
                (cur->val < prev->val && cur->val < cur->next->val))
                crit.push_back(idx);
            prev = cur; cur = cur->next; idx++;
        }
        if (crit.size() < 2) return {-1, -1};
        int mn = crit[1] - crit[0];
        for (int i = 2; i < (int)crit.size(); i++) mn = min(mn, crit[i] - crit[i - 1]);
        return {mn, crit.back() - crit[0]};
    }
};
