// LeetCode 3134 - Find the Median of the Uniqueness Array
// https://leetcode.com/problems/find-the-median-of-the-uniqueness-array/

class Solution {
    fun medianOfUniquenessArray(nums: IntArray): Int {
        var n = nums.size
        var m = (1L + n) * n / 2
        var lo = 1
        var hi = n
        while (lo < hi) {
            var mid = lo + (hi - lo) / 2
            if (check(nums, n, m, mid)) hi = mid
            else lo = mid + 1
        }
        return lo
    }

    private fun check(nums: IntArray, n: Int, m: Long, mx: Int): Boolean {
        var cnt = HashMap<Int, Int>()
        var l = 0
        var k = 0
        for (r in 0 until n) {
            cnt[nums[r]] = cnt.getOrDefault(nums[r], 0) + 1
            while (cnt.size > mx) {
                var y = nums[l++]
                var nv = cnt[y] - 1
                if (nv == 0) cnt.remove(y)
                else cnt[y] = nv
            }
            k += r - l + 1
            if (k >= (m + 1) / 2) return true
        }
        return false
    }
}
