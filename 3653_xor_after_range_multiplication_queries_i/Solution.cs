// LeetCode 3653 - XOR After Range Multiplication Queries I
// https://leetcode.com/problems/xor-after-range-multiplication-queries-i/

public class Solution {
    public int XorAfterQueries(int[] nums, int[][] queries) {
        const int mod = 1000000007;
        foreach (var q in queries) {
            int l = q[0], r = q[1], k = q[2], v = q[3];
            for (int idx = l; idx <= r; idx += k) nums[idx] = (int)(1L * nums[idx] * v % mod);
        }
        int ans = 0;
        foreach (int x in nums) ans ^= x;
        return ans;
    }
}
