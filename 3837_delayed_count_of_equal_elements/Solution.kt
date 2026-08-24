// LeetCode 3837 - Delayed Count Of Equal Elements
// https://leetcode.com/problems/delayed-count-of-equal-elements/

class Solution {
    fun delayedCount(nums: IntArray, k: Int): IntArray {
        var n = nums.size
        var cnt = HashMap<Int, Int>()
        var ans = IntArray(n)
        for (i in n - k - 2 downTo 0) {
            var key = nums[i + k + 1]
            cnt[key] = cnt.getOrDefault(key, 0 + 1)
            ans[i] = cnt.getOrDefault(nums[i], 0)
        }
        return ans
    }
}
