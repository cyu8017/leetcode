// LeetCode 2317 - Maximum XOR After Operations
// https://leetcode.com/problems/maximum-xor-after-operations/

class Solution {
    fun maximumXOR(nums: IntArray): Int {
        var ans = 0
        for (x in nums) ans = ans or x
        return ans
    }
}
