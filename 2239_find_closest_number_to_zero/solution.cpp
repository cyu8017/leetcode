// LeetCode 2239 - Find Closest Number to Zero
// https://leetcode.com/problems/find-closest-number-to-zero/

#include <vector>
#include <cstdlib>

class Solution {
public:
    int findClosestNumber(std::vector<int>& nums) {
        int ans = nums[0];
        for (int x : nums) {
            if (std::abs(x) < std::abs(ans) || (std::abs(x) == std::abs(ans) && x > ans)) ans = x;
        }
        return ans;
    }
};
