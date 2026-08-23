// LeetCode 3698 - Split Array With Minimum Difference
// https://leetcode.com/problems/split-array-with-minimum-difference/

#include <algorithm>
#include <climits>
#include <cstdlib>
#include <vector>

class Solution {
public:
    long long splitArray(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<long long> s(n);
        std::vector<bool> f(n, true), g(n, true);
        s[0] = nums[0];
        for (int i = 1; i < n; i++) {
            s[i] = s[i - 1] + nums[i];
            f[i] = f[i - 1];
            if (nums[i] <= nums[i - 1]) f[i] = false;
        }
        for (int i = n - 2; i >= 0; i--) {
            g[i] = g[i + 1];
            if (nums[i] <= nums[i + 1]) g[i] = false;
        }
        const long long inf = LLONG_MAX / 4;
        long long ans = inf;
        for (int i = 0; i < n - 1; i++) {
            if (f[i] && g[i + 1]) {
                long long s1 = s[i], s2 = s[n - 1] - s[i];
                ans = std::min(ans, std::llabs(s1 - s2));
            }
        }
        return ans < inf ? ans : -1;
    }
};
