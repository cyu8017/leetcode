// LeetCode 3578 - Count Partitions With Max-Min Difference at Most K
// https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/

#include <set>
#include <vector>

class Solution {
public:
    int countPartitions(std::vector<int>& nums, int k) {
        const int mod = 1000000007;
        std::multiset<int> sl;
        int n = (int)nums.size();
        std::vector<int> f(n + 1), g(n + 1);
        f[0] = g[0] = 1;
        for (int l = 1, r = 1; r <= n; r++) {
            sl.insert(nums[r - 1]);
            while (*sl.rbegin() - *sl.begin() > k) {
                sl.erase(sl.find(nums[l - 1]));
                l++;
            }
            f[r] = g[r - 1];
            if (l >= 2) f[r] = (f[r] - g[l - 2] + mod) % mod;
            g[r] = (g[r - 1] + f[r]) % mod;
        }
        return f[n];
    }
};
