// LeetCode 2499 - Minimum Total Cost to Make Arrays Unequal
// https://leetcode.com/problems/minimum-total-cost-to-make-arrays-unequal/

import java.util.HashMap

class Solution {
    fun minimumTotalCost(nums1: IntArray, nums2: IntArray): Long {
            var n: Int = nums1.size
            var freq: MutableMap<Int, Int> = HashMap()
            var ans: Long = 0
            var same: Int = 0
            var i: Int = 0
    while (i < n) {
    
                if (nums1[i] == nums2[i]) {
                    same = same + 1
                    freq.put(nums1[i], freq.getOrDefault(nums1[i], 0) + 1)
                    ans +=i
                }
    
    i = i + 1
    }
            var maxFreq: Int = 0
            var maxVal: Int = 0
            for (kv in freq.entrySet()) {
                if (kv.getValue() > maxFreq) {
                    maxFreq = kv.getValue()
                    maxVal = kv.getKey()
                }
            }
            var need: Int = maxFreq * 2 - same
            if (need <= 0) return ans
            var i: Int = 0
    while (i < n && need > 0) {
    
                if (nums1[i] != nums2[i] && nums1[i] != maxVal && nums2[i] != maxVal) {
                    ans +=i
                    need = need - 1
                }
    
    i = i + 1
    }
            return if (need > 0) -1 else ans
    }
}
