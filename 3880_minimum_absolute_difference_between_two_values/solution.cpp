// LeetCode 3880 - Minimum Absolute Difference Between Two Values
// https://leetcode.com/problems/minimum-absolute-difference-between-two-values/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minAbsoluteDifference(std::vector<int>& nums) {
        int n = (int)nums.size();
        int ans = n + 1;
        int last[3] = {-ans, -ans, -ans};
        for (int i = 0; i < n; i++) {
            int x = nums[i];
            if (x != 0) {
                ans = std::min(ans, i - last[3 - x]);
                last[x] = i;
            }
        }
        if (ans > n) return -1;
        return ans;
    }
};
