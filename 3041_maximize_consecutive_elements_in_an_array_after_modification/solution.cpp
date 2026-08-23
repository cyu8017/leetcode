// LeetCode 3041 - Maximize Consecutive Elements in an Array After Modification
// https://leetcode.com/problems/maximize-consecutive-elements-in-an-array-after-modification/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int maxSelectedElements(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        std::unordered_map<int, int> dp;
        int ans = 0;
        for (int num : nums) {
            dp[num + 1] = dp[num] + 1;
            dp[num] = dp[num - 1] + 1;
            ans = std::max({ans, dp[num], dp[num + 1]});
        }
        return ans;
    }
};
