// LeetCode 3551 - Minimum Swaps to Sort by Digit Sum
// https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/

class Solution {
    fun f(x0: Int): Int {
        var x = x0
        var s = 0
        while (x != 0) {
            s += x % 10
            x /= 10
        }
        return s
    }

    fun minSwaps(nums: IntArray): Int {
        val n = nums.size
        val arr = Array(n) { IntArray(2) }
        for (i in 0 until n) arr[i] = intArrayOf(f(nums[i]), nums[i])
        arr.sortWith(compareBy({ it[0] }, { it[1] }))
        val d = HashMap<Int, Int>()
        for (i in 0 until n) d[arr[i][1]] = i
        val vis = BooleanArray(n)
        var ans = n
        for (i in 0 until n) {
            if (!vis[i]) {
                ans--
                var j = i
                while (!vis[j]) {
                    vis[j] = true
                    j = d[nums[j]]!!
                }
            }
        }
        return ans
    }
}
