// LeetCode 2439 - Minimize Maximum of Array
// https://leetcode.com/problems/minimize-maximum-of-array/

class Solution {
    fun minimizeArrayValue(nums: IntArray): Int {
            var sum: Long = 0
            var ans: Int = 0
            var i: Int = 0
    while (i < nums.size) {
    
                sum +=nums[i]
                var avg: Int = ((sum + i) / (i + 1))
                if (avg > ans) ans = avg
    
    i = i + 1
    }
            return ans
    }
}
