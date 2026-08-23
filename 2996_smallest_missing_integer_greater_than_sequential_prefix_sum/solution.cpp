// LeetCode 2996 - Smallest Missing Integer Greater Than Sequential Prefix Sum
// https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/

#include <vector>
#include <unordered_set>

class Solution {
public:
    int missingInteger(std::vector<int>& nums) {
        int sum = nums[0];
        for (int i = 1; i < (int)nums.size() && nums[i] == nums[i - 1] + 1; i++) {
            sum += nums[i];
        }
        std::unordered_set<int> seen(nums.begin(), nums.end());
        while (seen.count(sum)) sum++;
        return sum;
    }
};
