// LeetCode 2917 - Find the K-or of an Array
// https://leetcode.com/problems/find-the-k-or-of-an-array/

class Solution {
    fun findKOr(nums: IntArray, k: Int): Int {
        var ans = 0
        for (b in 0 until 31) {
            var cnt = 0
            for (v in nums) { if ((v & (1  shl  b)) != 0) cnt++ }
            if (cnt >= k) ans |= 1  shl  b
        }
        return ans
    }
}
