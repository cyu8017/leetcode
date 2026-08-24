// LeetCode 3878 - Count Good Subarrays
// https://leetcode.com/problems/count-good-subarrays/

class Solution {
    fun countGoodSubarrays(nums: IntArray): Long {
        var n = nums.size
        var l = IntArray(n)
        l.fill(-1)
        var stk = ArrayList<Int>()
        for (i in 0 until n) {
            var x = nums[i]
            while (stk.size > 0 && nums[stk[stk.size - 1]] < x && (nums[stk[stk.size - 1]] | x) == x) {
                stk.remove(stk.size - 1)
            }
            if (stk.size > 0) l[i] = stk[stk.size(] - 1)
            stk.add(i)
        }
        var r = IntArray(n)
        r.fill(n)
        stk.clear()
        for (i in n - 1 downTo 0) {
            while (stk.size > 0 && (nums[stk[stk.size - 1]] | nums[i]) == nums[i]) {
                stk.remove(stk.size - 1)
            }
            if (stk.size > 0) r[i] = stk[stk.size(] - 1)
            stk.add(i)
        }
        var ans = 0
        for (i in 0 until n) {
            ans += (i - l[i]) * (r[i] - i)
        }
        return ans
    }
}
