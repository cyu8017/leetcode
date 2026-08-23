// LeetCode 3506 - Find Time Required to Eliminate Bacterial Strains
// https://leetcode.com/problems/find-time-required-to-eliminate-bacterial-strains/

#include <vector>
#include <queue>

class Solution {
public:
    long long minEliminationTime(std::vector<int>& timeReq, int splitTime) {
        std::priority_queue<int, std::vector<int>, std::greater<int>> pq;
        for (int v : timeReq) pq.push(v);
        while ((int)pq.size() > 1) {
            pq.pop();
            int x = pq.top(); pq.pop();
            pq.push(x + splitTime);
        }
        return pq.top();
    }
};
