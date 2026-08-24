// LeetCode 2012 - Sum of Beauty in the Array
// https://leetcode.com/problems/sum-of-beauty-in-the-array/

class Solution {
    fun sumOfBeauties(nums: IntArray): Int {
var n: Int = nums.size
var prefixMax: IntArray = IntArray(n)
var suffixMin: IntArray = IntArray(n)
prefixMax[0] = nums[0]
for (i in 1 until n) {
prefixMax[i] = maxOf(prefixMax[i - 1], nums[i])
}
suffixMin[n - 1] = nums[n - 1]
for (i in n - 2 downTo 0) {
suffixMin[i] = minOf(suffixMin[i + 1], nums[i])
}
var ans: Int = 0
for (i in 1 until n - 1) {
if (prefixMax[i - 1] < nums[i] && nums[i] < suffixMin[i + 1]) {
ans += 2
}
else if (nums[i - 1] < nums[i] && nums[i] < nums[i + 1]) {
ans++
}
}
return ans
}
}
