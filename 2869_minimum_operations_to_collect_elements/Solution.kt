// LeetCode 2869 - Minimum Operations to Collect Elements
// https://leetcode.com/problems/minimum-operations-to-collect-elements/

class Solution {
    fun minOperations(nums: MutableList<Int>, k: Int): Int {
        var need = HashSet<Int>()
        for (i in 1..k) { need.add(i) }
        for (i in nums.size - 1 downTo 0) {
            need.remove(nums[i])
            if (need.isEmpty()) return nums.size - i
        }
        return nums.size
    }
}
