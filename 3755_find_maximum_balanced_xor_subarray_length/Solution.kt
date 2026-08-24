// LeetCode 3755 - Find Maximum Balanced Xor Subarray Length
// https://leetcode.com/problems/find_maximum_balanced_xor_subarray_length/

class Solution {
    fun maxBalancedSubarray(nums: IntArray): Int {
        var d = HashMap<Long, Int>()
        var a = 0
        var b = nums.size
        var ans = 0
        d[b] = -1
        for (i in 0 until nums.size) {
            a ^= nums[i]
            if (nums[i] % 2 == 0) { b = b + 1 }
            else b -= 1
            var key = (a  shl  32) | (b & 0xffffffffL)
            if (d.containsKey(key)) ans = maxOf(ans, i - d[key])
            else d[key] = i
        }
        return ans
    }
}
