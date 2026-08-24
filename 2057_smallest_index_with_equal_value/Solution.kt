// LeetCode 2057 - Smallest Index With Equal Value
// https://leetcode.com/problems/smallest-index-with-equal-value/

class Solution {
    fun smallestEqual(nums: IntArray): Int {
for (i in 0 until nums.size) {
if (i % 10 == nums[i]) {
return i
}
}
return -1
}
}
