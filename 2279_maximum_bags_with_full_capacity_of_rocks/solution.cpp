// LeetCode 2279 - Maximum Bags With Full Capacity of Rocks
// https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/

#include <vector>
#include <algorithm>

class Solution {
public:
    int maximumBags(std::vector<int>& capacity, std::vector<int>& rocks, int additionalRocks) {
        std::vector<int> need(capacity.size());
        for (size_t i = 0; i < capacity.size(); ++i) need[i] = capacity[i] - rocks[i];
        std::sort(need.begin(), need.end());
        int ans = 0;
        for (int n : need) {
            if (additionalRocks < n) break;
            additionalRocks -= n;
            ans++;
        }
        return ans;
    }
};
