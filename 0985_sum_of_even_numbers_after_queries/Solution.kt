// LeetCode 0985 - Sum of Even Numbers After Queries
// https://leetcode.com/problems/sum-of-even-numbers-after-queries/

class Solution {
    fun sumEvenAfterQueries(nums: IntArray, queries: Array<IntArray>): IntArray {
var even: Int = 0
for (x in nums) {
if (x % 2 == 0) {
even += x
}
}
var ans: IntArray = IntArray(queries.size)
for (qi in 0 until queries.size) {
var `val`: Int = queries[qi][0]
var i: Int = queries[qi][1]
if (nums[i] % 2 == 0) {
even -= nums[i]
}
nums[i] += val
if (nums[i] % 2 == 0) {
even += nums[i]
}
ans[qi] = even
}
return ans
}
}
