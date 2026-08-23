// LeetCode 3693 - Climbing Stairs II
// https://leetcode.com/problems/climbing-stairs-ii/

#include <algorithm>
#include <vector>

class Solution {
public:
    int climbStairs(int n, std::vector<int>& costs) {
        const int inf = (int)1e9;
        std::vector<int> f(n + 1, inf);
        f[0] = 0;
        for (int i = 1; i <= n; i++) {
            int x = costs[i - 1];
            for (int j = std::max(0, i - 3); j < i; j++) {
                f[i] = std::min(f[i], f[j] + x + (i - j) * (i - j));
            }
        }
        return f[n];
    }
};
