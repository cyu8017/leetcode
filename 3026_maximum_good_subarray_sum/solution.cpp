// LeetCode 3026 - Maximum Good Subarray Sum
// https://leetcode.com/problems/maximum-good-subarray-sum/

#include <algorithm>
#include <climits>
#include <unordered_map>
#include <vector>

class Solution {
public:
    long long maximumSubarraySum(std::vector<int>& nums, int k) {
        std::unordered_map<int, long long> p;
        p[nums[0]] = 0;
        long long s = 0;
        int n = (int)nums.size();
        long long ans = LLONG_MIN;
        for (int i = 0; i < n; i++) {
            s += nums[i];
            if (p.count(nums[i] - k)) ans = std::max(ans, s - p[nums[i] - k]);
            if (p.count(nums[i] + k)) ans = std::max(ans, s - p[nums[i] + k]);
            if (i + 1 == n) break;
            if (!p.count(nums[i + 1]) || s < p[nums[i + 1]]) p[nums[i + 1]] = s;
        }
        return ans == LLONG_MIN ? 0 : ans;
    }
};
