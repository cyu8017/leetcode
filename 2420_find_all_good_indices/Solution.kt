// LeetCode 2420 - Find All Good Indices
// https://leetcode.com/problems/find-all-good-indices/

import java.util.ArrayList

class Solution {
    fun goodIndices(nums: IntArray, k: Int): MutableList<Int> {
            var n: Int = nums.size
            var dec: IntArray = IntArray(n)
            var inc: IntArray = IntArray(n)
            dec[0] = 1
            var i: Int = 1
    while (i < n) {
    
                dec[i] = if (nums[i] <= nums[i - 1]) dec[i - 1] + 1 else 1
    i = i + 1
    }
            inc[n - 1] = 1
            var i: Int = n - 2
    while (i >= 0) {
    
                inc[i] = if (nums[i] <= nums[i + 1]) inc[i + 1] + 1 else 1
    i = i - 1
    }
            var ans: MutableList<Int> = ArrayList()
            var i: Int = k
    while (i < n - k) {
    
                if (dec[i - 1] >= k && inc[i + 1] >= k) ans.add(i)
    
    i = i + 1
    }
            return ans
    }
}
