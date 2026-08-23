// LeetCode 3065 - Minimum Operations to Exceed Threshold Value I
// https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-i/

#include <vector>

class Solution {
public:
    int minOperations(std::vector<int>& nums, int k) {
        int ans = 0;
        for (int x : nums) if (x < k) ans++;
        return ans;
    }
};
