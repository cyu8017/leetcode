// LeetCode 3825 - Longest Strictly Increasing Subsequence With Non Zero Bitwise And
// https://leetcode.com/problems/longest-strictly-increasing-subsequence-with-non-zero-bitwise-and/

#include <algorithm>
#include <vector>

class Solution {
    static int bitLen(unsigned x) {
        return x == 0 ? 0 : 32 - __builtin_clz(x);
    }

    static int lis(const std::vector<int>& arr) {
        std::vector<int> g;
        for (int x : arr) {
            auto it = std::lower_bound(g.begin(), g.end(), x);
            if (it == g.end()) g.push_back(x);
            else *it = x;
        }
        return (int)g.size();
    }

public:
    int longestSubsequence(std::vector<int>& nums) {
        int ans = 0;
        int mx = *std::max_element(nums.begin(), nums.end());
        int m = bitLen((unsigned)mx);
        for (int i = 0; i < m; i++) {
            std::vector<int> arr;
            for (int x : nums) {
                if ((x >> i) & 1) arr.push_back(x);
            }
            ans = std::max(ans, lis(arr));
        }
        return ans;
    }
};
