// LeetCode 3684 - Maximize Sum of At Most K Distinct Elements
// https://leetcode.com/problems/maximize-sum-of-at-most-k-distinct-elements/

class Solution {
    fun maxKDistinct(nums: IntArray, k: Int): IntArray {
        nums.sort()
        var n = nums.size
        var ans = ArrayList<Int>()
        for (i in n - 1 downTo 0) {
            if (i + 1 < n && nums[i] == nums[i + 1]) continue
            ans.add(nums[i])
            if (--k == 0) break
        }
        var res = IntArray(ans.size)
        for (i in 0 until ans.size) { res[i] = ans[i] }
        return res
    }
}
