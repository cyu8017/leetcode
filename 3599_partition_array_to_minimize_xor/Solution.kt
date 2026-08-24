// LeetCode 3599 - Partition Array to Minimize XOR
// https://leetcode.com/problems/partition-array-to-minimize-xor/

class Solution {
    fun minXor(nums: IntArray, k: Int): Int {
        var n = nums.size
        var g = IntArray(n + 1)
        for (i in 1..n) { g[i] = g[i - 1] ^ nums[i - 1] }
        val Inf = Int.MAX_VALUE / 2
        var f = arrayOfNulls<IntArray>(n + 1)
        for (i in 0..n) {
            f[i] = IntArray(k + 1)
            for (j in 0..k) { f[i][j] = Inf }
        }
        f[0][0] = 0
        for (i in 1..n) {
            for (j in 1..minOf(i, k)) {
                for (h in j - 1 until i) {
                    f[i][j] = minOf(f[i][j], maxOf(f[h][j - 1], g[i] ^ g[h]))
                }
            }
        }
        return f[n][k]
    }
}
