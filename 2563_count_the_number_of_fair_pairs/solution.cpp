// LeetCode 2563 - Count the Number of Fair Pairs
// https://leetcode.com/problems/count-the-number-of-fair-pairs/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long countFairPairs(std::vector<int>& nums, int lower, int upper) {
        std::sort(nums.begin(), nums.end());
        auto count = [&](int x) {
            long long ans = 0;
            int l = 0, r = (int)nums.size() - 1;
            while (l < r) {
                if (nums[l] + nums[r] <= x) {
                    ans += r - l;
                    l++;
                } else {
                    r--;
                }
            }
            return ans;
        };
        return count(upper) - count(lower - 1);
    }
};
