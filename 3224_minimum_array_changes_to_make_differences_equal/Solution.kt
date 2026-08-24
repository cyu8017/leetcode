// LeetCode 3224 - Minimum Array Changes to Make Differences Equal
// https://leetcode.com/problems/minimum-array-changes-to-make-differences-equal/

class Solution {
    fun minChanges(nums: IntArray, k: Int): Int {
        var d = IntArray(k + 2)
        var n = nums.size
        for (i in 0 until n / 2) {
            var x = nums[i]
            var y = nums[n - 1 - i]
            if (x > y) { val t = x; x = y; y = t }
            d[0] += 1
            d[y - x] -= 1
            d[y - x + 1] += 1
            var mx = maxOf(y, k - x)
            d[mx + 1] -= 1
            d[mx + 1] += 2
        }
        var ans = n
        var s = 0
        for (x in d) {
            s += x
            ans = minOf(ans, s)
        }
        return ans
    }
}
