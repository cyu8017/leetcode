// LeetCode 3878 - Count Good Subarrays
// https://leetcode.com/problems/count-good-subarrays/

#include <vector>

class Solution {
public:
    long long countGoodSubarrays(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<int> l(n, -1), stk;
        for (int i = 0; i < n; i++) {
            int x = nums[i];
            while (!stk.empty() && nums[stk.back()] < x && (nums[stk.back()] | x) == x) {
                stk.pop_back();
            }
            if (!stk.empty()) l[i] = stk.back();
            stk.push_back(i);
        }
        std::vector<int> r(n, n);
        stk.clear();
        for (int i = n - 1; i >= 0; i--) {
            while (!stk.empty() && (nums[stk.back()] | nums[i]) == nums[i]) {
                stk.pop_back();
            }
            if (!stk.empty()) r[i] = stk.back();
            stk.push_back(i);
        }
        long long ans = 0;
        for (int i = 0; i < n; i++) {
            ans += (long long)(i - l[i]) * (r[i] - i);
        }
        return ans;
    }
};
