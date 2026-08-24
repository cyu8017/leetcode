// LeetCode 2161 - Partition Array According to Given Pivot
// https://leetcode.com/problems/partition-array-according-to-given-pivot/

class Solution {
    fun pivotArray(nums: IntArray, pivot: Int): IntArray {
        var ans: IntArray = IntArray(nums.size)
        var i: Int = 0
        for (x in nums) if (x < pivot) ans[i++] = x
        for (x in nums) if (x == pivot) ans[i++] = x
        for (x in nums) if (x > pivot) ans[i++] = x
        return ans
    }
}
