// LeetCode 3489 - Zero Array Transformation IV
// https://leetcode.com/problems/zero-array-transformation-iv/

#include <vector>

class Solution {
    bool canSubsetSum(const std::vector<int>& vals, int target) {
        if (target == 0) return true;
        std::vector<char> dp(target + 1, 0);
        dp[0] = 1;
        for (int v : vals) {
            for (int s = target; s >= v; s--) if (dp[s - v]) dp[s] = 1;
        }
        return dp[target];
    }
public:
    int minZeroArray(std::vector<int>& nums, std::vector<std::vector<int>>& queries) {
        int n = (int)nums.size();
        auto ok = [&](int k) {
            for (int i = 0; i < n; i++) {
                if (nums[i] == 0) continue;
                std::vector<int> vals;
                for (int q = 0; q < k; q++) {
                    int l = queries[q][0], r = queries[q][1], v = queries[q][2];
                    if (l <= i && i <= r) vals.push_back(v);
                }
                if (!canSubsetSum(vals, nums[i])) return false;
            }
            return true;
        };
        if (ok(0)) return 0;
        int lo = 1, hi = (int)queries.size() + 1;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (mid <= (int)queries.size() && ok(mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo > (int)queries.size() ? -1 : lo;
    }
};
