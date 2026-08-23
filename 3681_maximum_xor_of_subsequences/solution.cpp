// LeetCode 3681 - Maximum XOR of Subsequences
// https://leetcode.com/problems/maximum-xor-of-subsequences/

#include <vector>

class Solution {
public:
    int maxXorSubsequences(std::vector<int>& nums) {
        std::vector<int> basis(32, 0);
        for (int x : nums) {
            int cur = x;
            for (int b = 31; b >= 0; b--) {
                if ((cur & (1 << b)) == 0) continue;
                if (basis[b] == 0) {
                    basis[b] = cur;
                    break;
                }
                cur ^= basis[b];
            }
        }
        int ans = 0;
        for (int b = 31; b >= 0; b--) {
            if ((ans ^ basis[b]) > ans) ans ^= basis[b];
        }
        return ans;
    }
};
