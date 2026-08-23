// LeetCode 3653 - XOR After Range Multiplication Queries I
// https://leetcode.com/problems/xor-after-range-multiplication-queries-i/

class Solution {
    public int xorAfterQueries(int[] nums, int[][] queries) {
        int mod = 1000000007;
        for (var q : queries) {
            int l = q[0], r = q[1], k = q[2], v = q[3];
            for (int idx = l; idx <= r; idx += k) nums[idx] = (int)(1L * nums[idx] * v % mod);
        }
        int ans = 0;
        for (int x : nums) ans ^= x;
        return ans;
    }
}
