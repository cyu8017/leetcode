// LeetCode 3660 - Jump Game IX
// https://leetcode.com/problems/jump-game-ix/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    std::vector<int> maxValue(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<int> ans(n), preMax(n);
        preMax[0] = nums[0];
        for (int i = 1; i < n; i++) preMax[i] = std::max(preMax[i - 1], nums[i]);
        int sufMin = INT_MAX / 2;
        for (int i = n - 1; i >= 0; i--) {
            if (preMax[i] > sufMin) ans[i] = ans[i + 1];
            else ans[i] = preMax[i];
            sufMin = std::min(sufMin, nums[i]);
        }
        return ans;
    }
};
