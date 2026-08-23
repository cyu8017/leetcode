// LeetCode 3854 - Minimum Operations To Make Array Parity Alternating
// https://leetcode.com/problems/minimum-operations-to-make-array-parity-alternating/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    std::vector<int> makeParityAlternating(std::vector<int>& nums) {
        if (nums.size() == 1) return {0, 0};
        int mn = *std::min_element(nums.begin(), nums.end());
        int mx = *std::max_element(nums.begin(), nums.end());
        auto f = [&](int k) {
            int cnt = 0, a = INT_MAX, b = INT_MIN;
            for (int i = 0; i < (int)nums.size(); i++) {
                int x = nums[i];
                if (((x - i) & 1) != k) {
                    cnt++;
                    if (x == mn) x++;
                    else if (x == mx) x--;
                }
                a = std::min(a, x);
                b = std::max(b, x);
            }
            return std::vector<int>{cnt, std::max(1, b - a)};
        };
        auto r0 = f(0), r1 = f(1);
        if (r0[0] != r1[0]) return r0[0] < r1[0] ? r0 : r1;
        return r0[1] <= r1[1] ? r0 : r1;
    }
};
