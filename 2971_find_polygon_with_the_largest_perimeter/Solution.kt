// LeetCode 2971 - Find Polygon With the Largest Perimeter
// https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/

class Solution {
    fun largestPerimeter(nums: IntArray): Long {
        nums.sort()
        var sum = 0
        for (v in nums) { sum += v }
        for (i in nums.size - 1 downTo 2) {
            sum -= nums[i]
            if (sum > nums[i]) return sum + nums[i]
        }
        return -1
    }
}
