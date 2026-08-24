// LeetCode 3877 - Minimum Removals To Achieve Target Xor
// https://leetcode.com/problems/minimum-removals-to-achieve-target-xor/

class Solution {
    fun minRemovals(nums: IntArray, target: Int): Int {
        var mx = 0
        for (x in nums) { mx = maxOf(mx, x) }
        var m = 0
        if (mx > 0) {
            var u = mx
            while (u != 0) { m++; u >>= 1; }
        }
        if ((1  shl  m) <= target) return -1
        var n = nums.size
        var N = 1  shl  m
        var f = IntArray(n + 1)[]
        for (i in 0..n) {
            f[i] = IntArray(N)
            f[i].fill(Int.MIN_VALUE)
        }
        f[0][0] = 0
        for (i in 1..n) {
            var x = nums[i - 1]
            for (j in 0 until N) {
                f[i][j] = f[i - 1][j]
                if (f[i - 1][j ^ x] != Int.MIN_VALUE) {
                    f[i][j] = maxOf(f[i][j], f[i - 1][j ^ x] + 1)
                }
            }
        }
        if (f[n][target] < 0) return -1
        return n - f[n][target]
    }
}
