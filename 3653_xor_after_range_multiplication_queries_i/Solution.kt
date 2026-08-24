// LeetCode 3653 - XOR After Range Multiplication Queries I
// https://leetcode.com/problems/xor-after-range-multiplication-queries-i/

class Solution {
    fun xorAfterQueries(nums: IntArray, queries: Array<IntArray>): Int {
        var mod = 1000000007
        for (q in queries) {
            var l = q[0]
            var r = q[1]
            var k = q[2]
            var v = q[3]
            run {
                var idx = l
                while (idx <= r) {
                    nums[idx] = (1L * nums[idx] * v % mod)
                    idx += k
                }
            }
        }
        var ans = 0
        for (x in nums) { ans ^= x }
        return ans
    }
}
