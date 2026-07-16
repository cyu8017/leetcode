// LeetCode 0215 - Kth Largest Element in an Array
// https://leetcode.com/problems/kth-largest-element-in-an-array/

import kotlin.random.Random

class Solution {
    fun findKthLargest(nums: IntArray, k: Int): Int {
        val target = nums.size - k
        var left = 0
        var right = nums.lastIndex
        while (left <= right) {
            val pivotIndex = partition(nums, left, right)
            when {
                pivotIndex == target -> return nums[pivotIndex]
                pivotIndex < target -> left = pivotIndex + 1
                else -> right = pivotIndex - 1
            }
        }
        return nums[left]
    }

    private fun partition(nums: IntArray, left: Int, right: Int): Int {
        val pivotIndex = left + Random.nextInt(right - left + 1)
        nums.swap(pivotIndex, right)
        var store = left
        for (i in left until right) {
            if (nums[i] <= nums[right]) {
                nums.swap(store, i)
                store++
            }
        }
        nums.swap(store, right)
        return store
    }

    private fun IntArray.swap(i: Int, j: Int) {
        val temp = this[i]
        this[i] = this[j]
        this[j] = temp
    }
}
