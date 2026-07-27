// LeetCode 1636 - Sort Array by Increasing Frequency
// https://leetcode.com/problems/sort-array-by-increasing-frequency/

class Solution {
    fun frequencySort(nums: IntArray): IntArray {
        val count = HashMap<Int, Int>()
        for (x in nums) count[x] = count.getOrDefault(x, 0) + 1
        return nums.sortedWith(compareBy({ count[it]!! }, { -it })).toIntArray()
    }
}
