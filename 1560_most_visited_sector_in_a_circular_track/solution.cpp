// LeetCode 1560 - Most Visited Sector in  a Circular Track
// https://leetcode.com/problems/most-visited-sector-in-a-circular-track/

#include <vector>

class Solution {
public:
    std::vector<int> mostVisited(int n, std::vector<int>& rounds) {
        const int start = rounds.front();
        const int end = rounds.back();
        std::vector<int> result;
        if (start <= end) {
            for (int i = start; i <= end; ++i) {
                result.push_back(i);
            }
        } else {
            for (int i = 1; i <= end; ++i) {
                result.push_back(i);
            }
            for (int i = start; i <= n; ++i) {
                result.push_back(i);
            }
        }
        return result;
    }
};
