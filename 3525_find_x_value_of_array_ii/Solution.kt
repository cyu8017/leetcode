// LeetCode 3525 - Find X Value of Array II
// https://leetcode.com/problems/find-x-value-of-array-ii/

class Solution {
    fun resultArray(nums: IntArray, k: Int, queries: Array<IntArray>): IntArray {
        var n = nums.size
        var ans = IntArray(queries.size)
        for (qi in 0 until queries.size) {
            var idx = queries[qi][0]
            var `val` = queries[qi][1]
            var start = queries[qi][2]
            var x = queries[qi][3]
            nums[idx] = val
            var prod = 1
            var cnt = 0
            for (i in start until n) {
                prod = prod * (nums[i] % k) % k
                if (prod == x) cn{ t = t + 1 }
            }
            ans[qi] = cnt
        }
        return ans
    }
}
