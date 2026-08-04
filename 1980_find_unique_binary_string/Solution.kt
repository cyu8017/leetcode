// LeetCode 1980
// https://leetcode.com/problems/find-unique-binary-string/

class Solution {
    fun findDifferentBinaryString(nums: Array<String>): String {
        val s = nums.toHashSet()
        val n = nums.size
        val sb = StringBuilder()
        for (i in 0 until n) sb.append(if (nums[i][i] == '0') '1' else '0')
        val cand = sb.toString()
        if (cand !in s) return cand
        for (i in 0 until (1 shl n)) {
            val c = Integer.toBinaryString(i).padStart(n, '0')
            if (c !in s) return c
        }
        return "0".repeat(n)
    }
}
