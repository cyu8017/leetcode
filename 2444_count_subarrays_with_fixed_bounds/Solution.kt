// LeetCode 2444 - Count Subarrays With Fixed Bounds
// https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

class Solution {
    fun countSubarrays(nums: IntArray, minK: Int, maxK: Int): Long {
            var ans: Long = 0
            var imin: Int = -1
            var imax: Int = -1
            var ibad: Int = -1
            var i: Int = 0
    while (i < nums.size) {
    
                var x: Int = nums[i]
                if (x < minK || x > maxK) ibad = i
                if (x == minK) imin = i
                if (x == maxK) imax = i
                var bound: Int = if (imin < imax) imin else imax
                if (bound > ibad) ans += bound - ibad
    
    i = i + 1
    }
            return ans
    }
}
