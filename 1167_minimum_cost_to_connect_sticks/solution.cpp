// LeetCode 1167 - Minimum Cost to Connect Sticks
// https://leetcode.com/problems/minimum-cost-to-connect-sticks/

#include <queue>
#include <vector>

class Solution {
public:
    int connectSticks(std::vector<int>& sticks) {
        if (sticks.size() <= 1) return 0;
        std::priority_queue<int, std::vector<int>, std::greater<int>> pq(sticks.begin(), sticks.end());
        int ans = 0;
        while (pq.size() > 1) {
            int cost = pq.top(); pq.pop();
            cost += pq.top(); pq.pop();
            ans += cost;
            pq.push(cost);
        }
        return ans;
    }
};
