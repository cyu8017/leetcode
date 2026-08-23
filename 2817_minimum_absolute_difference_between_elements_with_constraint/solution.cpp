// LeetCode 2817 - Minimum Absolute Difference Between Elements With Constraint
// https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/

#include <algorithm>
#include <climits>
#include <cstdlib>
#include <set>
#include <vector>

class Solution {
public:
    int minAbsoluteDifference(std::vector<int>& nums, int x) {
        if (x == 0) {
            int ans = INT_MAX;
            for (int i = 1; i < (int)nums.size(); i++)
                ans = std::min(ans, std::abs(nums[i] - nums[i - 1]));
            return ans;
        }
        int ans = INT_MAX;
        std::set<int> arr;
        for (int i = x; i < (int)nums.size(); i++) {
            arr.insert(nums[i - x]);
            int cur = nums[i];
            auto it = arr.lower_bound(cur);
            if (it != arr.end()) ans = std::min(ans, *it - cur);
            if (it != arr.begin()) ans = std::min(ans, cur - *std::prev(it));
        }
        return ans;
    }
};
