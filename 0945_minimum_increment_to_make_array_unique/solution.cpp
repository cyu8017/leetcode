// LeetCode 0945 - Minimum Increment to Make Array Unique
// https://leetcode.com/problems/minimum-increment-to-make-array-unique/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minIncrementForUnique(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        int ans = 0;
        for (int i = 1; i < (int)nums.size(); i++) {
            if (nums[i] <= nums[i - 1]) {
                int need = nums[i - 1] + 1;
                ans += need - nums[i];
                nums[i] = need;
            }
        }
        return ans;
    }
};
