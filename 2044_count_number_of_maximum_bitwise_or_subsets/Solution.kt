// LeetCode 2044 - Count Number of Maximum Bitwise-OR Subsets
// https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/

class Solution {
    private var ans: Int = 0
    private var maxOr: Int = 0
    private lateinit var nums: IntArray

    fun countMaxOrSubsets(nums: IntArray): Int {
this.nums = nums
maxOr = 0
ans = 0
for (x in nums) {
maxOr |= x
}
dfs(0, 0)
return ans
}

    private fun dfs(i: Int, cur: Int) {
if (i == nums.size) {
if (cur == maxOr) {
ans++
}
return
}
dfs(i + 1, cur)
dfs(i + 1, cur | nums[i])
}
}
