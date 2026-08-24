// LeetCode 2036 - Maximum Alternating Subarray Sum
// https://leetcode.com/problems/maximum-alternating-subarray-sum/

class Solution {
    fun maximumAlternatingSubarraySum(nums: IntArray): Long {
var ans: Long = Long.MIN_VALUE
var even: Long = 0
var odd: Long = 0
for (i in 0 until nums.size) {
var x: Long = nums[i]
if (i % 2 == 0) {
even += x
}
else {
even = maxOf(0L, even - x)
}
ans = maxOf(ans, even)
}
odd = 0
for (i in 1 until nums.size) {
var x: Long = nums[i]
if (i % 2 == 1) {
odd += x
}
else {
odd = maxOf(0L, odd - x)
}
ans = maxOf(ans, odd)
}
return ans
}
}
