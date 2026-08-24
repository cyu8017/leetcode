// LeetCode 3202 - Find the Maximum Length of Valid Subsequence II
// https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/

class Solution {
    fun maximumLength(nums: IntArray, k: Int): Int {
        var f = IntArray(k)[]
        for (i in 0 until k) { f[i] = IntArray(k) }
        var ans = 0
        for (raw in nums) {
            var x = raw % k
            for (j in 0 until k) {
                var y = (j - x + k) % k
                f[x][y] = f[y][x] + 1
                ans = maxOf(ans, f[x][y])
            }
        }
        return ans
    }
}
