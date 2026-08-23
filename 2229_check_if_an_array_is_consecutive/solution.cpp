// LeetCode 2229 - Check if an Array Is Consecutive
// https://leetcode.com/problems/check-if-an-array-is-consecutive/

#include <vector>
#include <unordered_set>
#include <algorithm>

class Solution {
public:
    bool isConsecutive(std::vector<int>& nums) {
        int mn = nums[0], mx = nums[0];
        std::unordered_set<int> seen;
        for (int x : nums) {
            if (!seen.insert(x).second) return false;
            mn = std::min(mn, x);
            mx = std::max(mx, x);
        }
        return mx - mn + 1 == (int)nums.size();
    }
};
