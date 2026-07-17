// LeetCode 1701 - Average Waiting Time
// https://leetcode.com/problems/average-waiting-time/

#include <algorithm>
#include <vector>

class Solution {
public:
    double averageWaitingTime(std::vector<std::vector<int>>& customers) {
        long long current = 0;
        long long total = 0;
        for (const auto& customer : customers) {
            current = std::max(current, (long long)customer[0]) + customer[1];
            total += current - customer[0];
        }
        return (double)total / customers.size();
    }
};
