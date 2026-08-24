// LeetCode 3867 - Sum Of Gcd Of Formed Pairs
// https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/

class Solution {
    fun Gcd(a: Int, b: Int): Int {
        while (b != 0) {
            var t = a % b
            a = b
            b = t
        }
        return a
    }

    fun gcdSum(nums: IntArray): Long {
        var n = nums.size
        var prefixGcd = IntArray(n)
        var mx = 0
        for (i in 0 until n) {
            mx = maxOf(mx, nums[i])
            prefixGcd[i] = Gcd(nums[i], mx)
        }
        prefixGcd.sort()
        var ans = 0
        for (i in 0 until n / 2) { ans += Gcd(prefixGcd[i], prefixGcd[n - i - 1]) }
        return ans
    }
}
