// LeetCode 1199 - Minimum Time to Build Blocks
// https://leetcode.com/problems/minimum-time-to-build-blocks/

#include <queue>
#include <vector>

class Solution {
public:
    int minBuildTime(std::vector<int>& blocks, int split) {
        std::priority_queue<int, std::vector<int>, std::greater<int>> pq(blocks.begin(), blocks.end());
        while (pq.size() > 1) {
            pq.pop();
            int b = pq.top(); pq.pop();
            pq.push(b + split);
        }
        return pq.top();
    }
};
