// LeetCode 0496 - Next Greater Element I
// https://leetcode.com/problems/next-greater-element-i/

class Solution {
    fun nextGreaterElement(nums1: IntArray, nums2: IntArray): IntArray {
        val nextGreater = mutableMapOf<Int, Int>()
        val stack = ArrayDeque<Int>()
        for (num in nums2) {
            while (stack.isNotEmpty() && stack.last() < num) {
                nextGreater[stack.removeLast()] = num
            }
            stack.addLast(num)
        }
        return IntArray(nums1.size) { index -> nextGreater.getOrDefault(nums1[index], -1) }
    }
}
