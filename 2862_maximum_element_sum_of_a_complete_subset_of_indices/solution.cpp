// LeetCode 2862 - Maximum Element-Sum of a Complete Subset of Indices
// https://leetcode.com/problems/maximum-element-sum-of-a-complete-subset-of-indices/

#include <unordered_map>
#include <vector>

class Solution {
public:
    long long maximumSum(std::vector<int>& nums) {
        int n = (int)nums.size();
        auto squareFree = [](int x) {
            int res = 1;
            for (int p = 2; p * p <= x; p++) {
                int cnt = 0;
                while (x % p == 0) {
                    x /= p;
                    cnt++;
                }
                if (cnt % 2 == 1) res *= p;
            }
            if (x > 1) res *= x;
            return res;
        };
        std::unordered_map<int, long long> groups;
        long long ans = 0;
        for (int i = 1; i <= n; i++) {
            int sf = squareFree(i);
            groups[sf] += nums[i - 1];
            if (groups[sf] > ans) ans = groups[sf];
        }
        return ans;
    }
};
