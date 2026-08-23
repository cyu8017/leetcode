// LeetCode 3381 - Maximum Subarray Sum With Length Divisible by K
// https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/

#include <cstdint>
#include <vector>

class Solution {
public:
    long long maxSubarraySum(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        std::vector<long long> pref(n + 1);
        for (int i = 0; i < n; i++) pref[i + 1] = pref[i] + nums[i];
        const long long INF = 1LL << 62;
        std::vector<long long> best(k, INF);
        best[0] = 0;
        long long ans = -(1LL << 62);
        for (int i = 1; i <= n; i++) {
            int r = i % k;
            if (best[r] != INF) {
                long long cand = pref[i] - best[r];
                if (cand > ans) ans = cand;
            }
            if (pref[i] < best[r]) best[r] = pref[i];
        }
        return ans;
    }
};
