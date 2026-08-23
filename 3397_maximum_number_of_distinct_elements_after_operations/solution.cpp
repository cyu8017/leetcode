// LeetCode 3397 - Maximum Number of Distinct Elements After Operations
// https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int maxDistinctElements(std::vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end());
        int ans = 0;
        long long prev = LLONG_MIN / 2;
        for (int x : nums) {
            long long cur = x - k;
            if (cur <= prev) cur = prev + 1;
            if (cur > x + k) continue;
            ans++;
            prev = cur;
        }
        return ans;
    }
};
