// LeetCode 0995 - Minimum Number of K Consecutive Bit Flips
// https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/

class Solution {
    fun minKBitFlips(nums: IntArray, k: Int): Int {
var n: Int = nums.size
var flip: IntArray = IntArray(n)
var ans: Int = 0
var flipped: Int = 0
for (i in 0 until n) {
if (i >= k) {
flipped ^= flip[i - k]
}
if (nums[i] == flipped) {
if (i + k > n) {
return -1
}
ans++
flipped ^= 1
flip[i] = 1
}
}
return ans
}
}
