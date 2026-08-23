// LeetCode 3653 - XOR After Range Multiplication Queries I
// https://leetcode.com/problems/xor-after-range-multiplication-queries-i/

#include <vector>

class Solution {
public:
    int xorAfterQueries(std::vector<int>& nums, std::vector<std::vector<int>>& queries) {
        const int mod = 1000000007;
        for (auto& q : queries) {
            int l = q[0], r = q[1], k = q[2], v = q[3];
            for (int idx = l; idx <= r; idx += k) nums[idx] = 1LL * nums[idx] * v % mod;
        }
        int ans = 0;
        for (int x : nums) ans ^= x;
        return ans;
    }
};
