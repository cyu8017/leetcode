// LeetCode 3177 - Find the Maximum Length of a Good Subsequence II
// https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-ii/

#include <vector>
#include <unordered_map>
#include <array>
#include <algorithm>

class Solution {
public:
    int maximumLength(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        std::vector<std::vector<int>> f(n, std::vector<int>(k + 1));
        std::vector<std::unordered_map<int, int>> mp(k + 1);
        std::vector<std::array<int, 3>> g(k + 1);
        int ans = 0;
        for (int i = 0; i < n; i++) {
            for (int h = 0; h <= k; h++) {
                f[i][h] = mp[h][nums[i]];
                if (h > 0) {
                    if (g[h - 1][0] != nums[i]) f[i][h] = std::max(f[i][h], g[h - 1][1]);
                    else f[i][h] = std::max(f[i][h], g[h - 1][2]);
                }
                f[i][h]++;
                mp[h][nums[i]] = std::max(mp[h][nums[i]], f[i][h]);
                if (g[h][0] != nums[i]) {
                    if (f[i][h] >= g[h][1]) {
                        g[h][2] = g[h][1];
                        g[h][1] = f[i][h];
                        g[h][0] = nums[i];
                    } else if (f[i][h] > g[h][2]) {
                        g[h][2] = f[i][h];
                    }
                } else if (f[i][h] > g[h][1]) {
                    g[h][1] = f[i][h];
                }
                ans = std::max(ans, f[i][h]);
            }
        }
        return ans;
    }
};
