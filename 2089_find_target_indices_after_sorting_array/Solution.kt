// LeetCode 2089 - Find Target Indices After Sorting Array
// https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution {
    fun targetIndices(nums: IntArray, target: Int): MutableList<Int> {
var less: Int = 0
var eq: Int = 0
for (x in nums) {
if (x < target) {
less++
}
else if (x == target) {
eq++
}
}
var ans: MutableList<Int> = ArrayList(eq)
for (i in 0 until eq) {
ans.add(less + i)
}
return ans
}
}
