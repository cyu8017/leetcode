// LeetCode 2488 - Count Subarrays With Median K
// https://leetcode.com/problems/count-subarrays-with-median-k/

import java.util.HashMap

class Solution {
    fun countSubarrays(nums: IntArray, k: Int): Int {
            var pos: Int = 0
            var i: Int = 0
    while (i < nums.size) {
    
                if (nums[i] == k) {
                    pos = i
                    break
                }
    
    i = i + 1
    }
            var bal: MutableMap<Int, Int> = HashMap()
            bal.put(0, 1)
            var cur: Int = 0
            var i: Int = pos - 1
    while (i >= 0) {
    
                cur +=if (nums[i] < k) -1 else 1
                bal.put(cur, bal.getOrDefault(cur, 0) + 1)
    
    i = i - 1
    }
            var ans: Int = bal.getOrDefault(0, 0) + bal.getOrDefault(1, 0)
            cur = 0
            var i: Int = pos + 1
    while (i < nums.size) {
    
                cur +=if (nums[i] < k) -1 else 1
                ans +=bal.getOrDefault(-cur, 0) + bal.getOrDefault(1 - cur, 0)
    
    i = i + 1
    }
            return ans
    }
}
