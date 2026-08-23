// LeetCode 2602 - Minimum Operations to Make All Array Elements Equal
// https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<long long> minOperations(std::vector<int>& nums, std::vector<int>& queries) {
        std::sort(nums.begin(), nums.end());
        int n = (int)nums.size();
        std::vector<long long> pref(n + 1);
        for (int i = 0; i < n; ++i) pref[i + 1] = pref[i] + nums[i];
        std::vector<long long> ans(queries.size());
        for (size_t qi = 0; qi < queries.size(); ++qi) {
            int q = queries[qi];
            int i = (int)(std::lower_bound(nums.begin(), nums.end(), q) - nums.begin());
            long long left = (long long)q * i - pref[i];
            long long right = pref[n] - pref[i] - (long long)q * (n - i);
            ans[qi] = left + right;
        }
        return ans;
    }
};
