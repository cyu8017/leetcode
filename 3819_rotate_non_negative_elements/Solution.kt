// LeetCode 3819 - Rotate Non Negative Elements
// https://leetcode.com/problems/rotate_non_negative_elements/

class Solution {
    fun rotateElements(nums: IntArray, k: Int): IntArray {
        val t = ArrayList<Int>()
        for (x in nums) if (x >= 0) t.add(x)
        val m = t.size
        if (m == 0) return nums
        val d = IntArray(m)
        for (i in 0 until m) d[((i - k) % m + m) % m] = t[i]
        var j = 0
        for (i in nums.indices) {
            if (nums[i] >= 0) nums[i] = d[j++]
        }
        return nums
    }
}
