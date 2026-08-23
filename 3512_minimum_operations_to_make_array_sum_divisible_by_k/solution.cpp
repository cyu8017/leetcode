// LeetCode 3512 - Minimum Operations to Make Array Sum Divisible by K
// https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/

#include <vector>

class Solution {
public:
    int minOperations(std::vector<int>& nums, int k) {
        int ans = 0;
        for (int x : nums) ans = (ans + x) % k;
        return ans;
    }
};
