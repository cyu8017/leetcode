// LeetCode 2926 - Maximum Balanced Subsequence Sum
// https://leetcode.com/problems/maximum-balanced-subsequence-sum/

#include <algorithm>
#include <vector>

class Solution {
public:
    long long maxBalancedSubsequenceSum(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<int> keys(n), uniq;
        for (int i = 0; i < n; i++) keys[i] = nums[i] - i;
        uniq = keys;
        std::sort(uniq.begin(), uniq.end());
        uniq.erase(std::unique(uniq.begin(), uniq.end()), uniq.end());
        auto idxOf = [&](int v) {
            return (int)(std::lower_bound(uniq.begin(), uniq.end(), v) - uniq.begin()) + 1;
        };
        const long long negInf = -(1LL << 60);
        std::vector<long long> bit(uniq.size() + 2, negInf);
        auto update = [&](int i, long long val) {
            for (; i < (int)bit.size(); i += i & -i)
                if (val > bit[i]) bit[i] = val;
        };
        auto query = [&](int i) {
            long long best = negInf;
            for (; i > 0; i -= i & -i)
                if (bit[i] > best) best = bit[i];
            return best;
        };
        long long ans = negInf;
        for (int i = 0; i < n; i++) {
            int id = idxOf(keys[i]);
            long long best = query(id);
            long long cur = nums[i];
            if (best > negInf / 2) {
                long long cand = best + nums[i];
                if (cand > cur) cur = cand;
            }
            update(id, cur);
            if (cur > ans) ans = cur;
        }
        return ans;
    }
};
