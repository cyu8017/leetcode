// LeetCode 2016 - Maximum Difference Between Increasing Elements
// https://leetcode.com/problems/maximum-difference-between-increasing-elements/

class Solution {
    fun maximumDifference(nums: IntArray): Int {
var ans: Int = -1
var mn: Int = nums[0]
for (i in 1 until nums.size) {
if (nums[i] > mn) {
ans = maxOf(ans, nums[i] - mn)
}
else {
mn = nums[i]
}
}
return ans
}
}
