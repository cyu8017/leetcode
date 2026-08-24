// LeetCode 3912 - Valid Elements In An Array
// https://leetcode.com/problems/valid-elements-in-an-array/

class Solution {
    fun findValidElements(nums: IntArray): IntArray {
        var n = nums.size
        var right = IntArray(n)
        right[n - 1] = nums[n - 1]
        run {
            var i = n - 2
            while (i >= 0) {
                right[i] = maxOf(right[i + 1], nums[i])
                i--
            }
        }
        var left = 0
        var ans = ArrayList<Int>()
        for (i in 0 until n) {
            var x = nums[i]
            if (x > left || i == n - 1 || x > right[i + 1]) ans.add(x)
            left = maxOf(left, x)
        }
        var out = IntArray(ans.size)
        for (i in 0 until ans.size) { out[i] = ans[i] }
        return out
    }
}
