// LeetCode 1674 - Minimum Moves to Make Array Complementary
// https://leetcode.com/problems/minimum-moves-to-make-array-complementary/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int minMoves(std::vector<int>& nums, int limit) {
        int n = static_cast<int>(nums.size());
        std::vector<int> d(2 * limit + 2, 0);
        for (int i = 0; i < n / 2; ++i) {
            int a = nums[i];
            int b = nums[n - 1 - i];
            int lo = std::min(a, b) + 1;
            int hi = std::max(a, b) + limit;
            int s = a + b;
            d[2] += 2;
            d[lo] -= 1;
            d[s] -= 1;
            d[s + 1] += 1;
            d[hi + 1] += 1;
        }
        int ans = INT_MAX;
        int cur = 0;
        for (int s = 2; s <= 2 * limit; ++s) {
            cur += d[s];
            ans = std::min(ans, cur);
        }
        return ans;
    }
};
