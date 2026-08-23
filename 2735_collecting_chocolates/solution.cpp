// LeetCode 2735 - Collecting Chocolates
// https://leetcode.com/problems/collecting-chocolates/

#include <vector>
#include <algorithm>
#include <climits>

class Solution {
public:
    long long minCost(std::vector<int>& nums, int x) {
        int n = (int)nums.size();
        std::vector<int> best = nums;
        long long ans = 0;
        for (int v : nums) ans += v;
        for (int rot = 1; rot < n; rot++) {
            long long cur = 1LL * rot * x;
            for (int i = 0; i < n; i++) {
                best[i] = std::min(best[i], nums[(i + rot) % n]);
                cur += best[i];
            }
            ans = std::min(ans, cur);
        }
        return ans;
    }
};
