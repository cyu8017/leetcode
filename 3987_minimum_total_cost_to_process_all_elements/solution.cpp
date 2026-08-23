// LeetCode 3987 - Minimum Total Cost to Process All Elements
// https://leetcode.com/problems/minimum-total-cost-to-process-all-elements/

#include <vector>

class Solution {
public:
    int minimumCost(std::vector<int>& nums, int k) {
        const long long mod = 1000000007LL;
        long long cnt = 0;
        long long cur = k;
        for (int x0 : nums) {
            long long x = x0;
            long long diff = x - cur;
            if (diff > 0) {
                long long m = (diff + k - 1) / k;
                cur += m * k;
                cnt += m;
            }
            cur -= x;
        }
        cnt %= mod;
        return (int)((cnt + 1) * cnt / 2 % mod);
    }
};
