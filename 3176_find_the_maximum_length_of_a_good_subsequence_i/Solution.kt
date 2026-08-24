// LeetCode 3176 - Find the Maximum Length of a Good Subsequence I
// https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-i/

class Solution {
    fun maximumLength(nums: IntArray, k: Int): Int {
        var n = nums.size
        var f = IntArray(n)[]
        for (i in 0 until n) { f[i] = IntArray(k + 1) }
        var ans = 0
        for (i in 0 until n) {
            for (h in 0 ..k) {
                for (j in 0 until i) {
                    if (nums[i] == nums[j]) f[i][h] = maxOf(f[i][h], f[j][h])
                    else if (h > 0) f[i][h] = maxOf(f[i][h], f[j][h - 1])
                }
                f[i][h]++
            }
            ans = maxOf(ans, f[i][k])
        }
        return ans
    }
}
