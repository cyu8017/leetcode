// LeetCode 2740 - Find the Value of the Partition
// https://leetcode.com/problems/find-the-value-of-the-partition/

#include <vector>
#include <algorithm>
#include <climits>

class Solution {
public:
    int findValueOfPartition(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        int ans = INT_MAX;
        for (int i = 1; i < (int)nums.size(); i++)
            ans = std::min(ans, nums[i] - nums[i - 1]);
        return ans;
    }
};
