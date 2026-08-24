// LeetCode 2461 - Maximum Sum of Distinct Subarrays With Length K
// https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

import java.util.HashMap

class Solution {
    fun maximumSubarraySum(nums: IntArray, k: Int): Long {
            var cnt: MutableMap<Int, Int> = HashMap()
            var sum: Long = 0
            var ans: Long = 0
            var i: Int = 0
    while (i < nums.size) {
    
                sum +=nums[i]
                cnt.put(nums[i], cnt.getOrDefault(nums[i], 0) + 1)
                if (i >= k) {
                    var y: Int = nums[i - k]
                    sum -=y
                    var c: Int = cnt.get(y) - 1
                    if (c == 0) cnt.remove(y)
                    else cnt.put(y, c)
                }
                if (i >= k - 1 && cnt.size == k && sum > ans) ans = sum
    
    i = i + 1
    }
            return ans
    }
}
