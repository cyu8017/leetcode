// LeetCode 3202 - Find the Maximum Length of Valid Subsequence II
// https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/

#include <vector>
#include <algorithm>

class Solution {
public:
    int maximumLength(std::vector<int>& nums, int k) {
        std::vector<std::vector<int>> f(k, std::vector<int>(k));
        int ans = 0;
        for (int x : nums) {
            x %= k;
            for (int j = 0; j < k; j++) {
                int y = (j - x + k) % k;
                f[x][y] = f[y][x] + 1;
                ans = std::max(ans, f[x][y]);
            }
        }
        return ans;
    }
};
