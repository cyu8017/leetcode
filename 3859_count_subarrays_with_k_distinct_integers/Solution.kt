// LeetCode 3859 - Count Subarrays With K Distinct Integers
// https://leetcode.com/problems/count-subarrays-with-k-distinct-integers/

class Solution {
    private var nums: IntArray? = null
    private var k: Int = 0
    private var m: Int = 0

    fun countSubarrays(nums: IntArray, k: Int, m: Int): Long {
        this.nums = nums
        this.k = k
        this.m = m
        return f(k) - f(k + 1)
    }

    private fun f(lim: Int): Long {
        var cnt = HashMap<Int, Int>()
        var ans = 0
        var l = 0
        var t = 0
        for (x in nums) {
            var c = cnt.getOrDefault(x, 0) + 1
            cnt[x] = c
            if (c == m) t++
            while (cnt.size >= lim && t >= k) {
                var y = nums[l++]
                var cy = cnt[y] - 1
                if (cy == m - 1) t--
                if (cy == 0) cnt.remove(y)
                else cnt[y] = cy
            }
            ans += l
        }
        return ans
    }
}
