// LeetCode 3511 - Make a Positive Array
// https://leetcode.com/problems/make-a-positive-array/

#include <vector>
#include <algorithm>

class Solution {
public:
    int makeArrayPositive(std::vector<int>& nums) {
        int ans = 0, l = -1;
        long long preMx = 0, s = 0;
        for (int r = 0; r < (int)nums.size(); r++) {
            s += nums[r];
            if (r - l > 2 && s <= preMx) {
                ans++;
                l = r;
                preMx = 0;
                s = 0;
            } else if (r - l >= 2) {
                preMx = std::max(preMx, s - nums[r] - nums[r - 1]);
            }
        }
        return ans;
    }
};
