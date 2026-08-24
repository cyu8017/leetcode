// LeetCode 0697 - Degree of an Array
// https://leetcode.com/problems/degree-of-an-array/

class Solution {
    fun findShortestSubArray(nums: IntArray): Int {
        val first = HashMap<Int, Int>()
        val last = HashMap<Int, Int>()
        val count = HashMap<Int, Int>()
        for (i in nums.indices) {
            first.putIfAbsent(nums[i], i)
            last[nums[i]] = i
            count[nums[i]] = count.getOrDefault(nums[i], 0) + 1
        }
        var degree = 0
        for (freq in count.values) degree = maxOf(degree, freq)
        var best = Int.MAX_VALUE
        for ((key, value) in count) {
            if (value == degree) best = minOf(best, last[key]!! - first[key]!! + 1)
        }
        return best
    }
}
