// LeetCode 1748 - Sum of Unique Elements
// https://leetcode.com/problems/sum-of-unique-elements/

class Solution {
    fun sumOfUnique(nums: IntArray): Int {
        val counts = HashMap<Int, Int>()
        for (value in nums) {
            counts[value] = (counts[value] ?: 0) + 1
        }
        var total = 0
        for ((value, count) in counts) {
            if (count == 1) {
                total += value
            }
        }
        return total
    }
}
