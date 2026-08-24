// LeetCode 2023 - Number of Pairs of Strings With Concatenation Equal to Target
// https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/

class Solution {
    fun numOfPairs(nums: Array<String>, target: String): Int {
var ans: Int = 0
for (i in 0 until nums.size) {
for (j in 0 until nums.size) {
if (i != j && (nums[i] + nums[j]).equals(target)) {
ans++
}
}
}
return ans
}
}
