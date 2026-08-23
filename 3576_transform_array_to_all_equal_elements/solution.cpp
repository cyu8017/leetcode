// LeetCode 3576 - Transform Array to All Equal Elements
// https://leetcode.com/problems/transform-array-to-all-equal-elements/

#include <vector>

class Solution {
public:
    bool canMakeEqual(std::vector<int>& nums, int k) {
        auto check = [&](int target, int kk) {
            int cnt = 0, sign = 1;
            for (int i = 0; i < (int)nums.size() - 1; i++) {
                int x = nums[i] * sign;
                if (x == target) sign = 1;
                else {
                    sign = -1;
                    cnt++;
                }
            }
            return cnt <= kk && nums.back() * sign == target;
        };
        return check(nums[0], k) || check(-nums[0], k);
    }
};
