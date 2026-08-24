// LeetCode 3717 - Minimum Operations to Make the Array Beautiful
// https://leetcode.com/problems/minimum-operations-to-make-the-array-beautiful/

class Solution {
    fun minOperations(nums: IntArray): Int {
        var f = HashMap<Int, Int>()
        f[nums[0]] = 0
        for (i in 1 until nums.size) {
            var x = nums[i]
            var g = HashMap<Int, Int>()
            for (e in f) {
                var pre = e.key
                var s = e.value
                var cur = (x + pre - 1) / pre * pre
                while (cur <= 100) {
                    var `val` = s + (cur - x)
                    var old = g[cur]
                    if (old == null || old > val) g[cur] = val
                    cur += pre
                }
            }
            f = g
        }
        var ans = Int.MAX_VALUE
        for (v in f.values) { ans = minOf(ans, v) }
        return ans
    }
}
