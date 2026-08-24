// LeetCode 2343 - Query Kth Smallest Trimmed Number
// https://leetcode.com/problems/query-kth-smallest-trimmed-number/

class Solution {
    fun smallestTrimmedNumbers(nums: Array<String>, queries: Array<IntArray>): IntArray {
        val n = nums.size
        val m = queries.size
        val ans = IntArray(m)
        for (qi in 0 until m) {
            val k = queries[qi][0]
            val trim = queries[qi][1]
            val arr = Array(n) { i ->
                val s = nums[i]
                arrayOf(s.substring(s.length - trim), i.toString())
            }
            arr.sortWith(compareBy({ it[0] }, { it[1].toInt() }))
            ans[qi] = arr[k - 1][1].toInt()
        }
        return ans
    }
}
