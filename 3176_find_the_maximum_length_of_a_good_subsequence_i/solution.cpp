// LeetCode 3176 - Find the Maximum Length of a Good Subsequence I
// https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-i/

#include <vector>
#include <algorithm>

class Solution {
public:
    int maximumLength(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        std::vector<std::vector<int>> f(n, std::vector<int>(k + 1));
        int ans = 0;
        for (int i = 0; i < n; i++) {
            for (int h = 0; h <= k; h++) {
                for (int j = 0; j < i; j++) {
                    if (nums[i] == nums[j]) f[i][h] = std::max(f[i][h], f[j][h]);
                    else if (h > 0) f[i][h] = std::max(f[i][h], f[j][h - 1]);
                }
                f[i][h]++;
            }
            ans = std::max(ans, f[i][k]);
        }
        return ans;
    }
};
