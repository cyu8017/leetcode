// LeetCode 1491 - Average Salary Excluding the Minimum and Maximum Salary
// https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

class Solution {
    fun average(salary: IntArray): Double {
        return (salary.sum().toLong() - salary.minOrNull()!! - salary.maxOrNull()!!).toDouble() / (salary.size - 2)
    }
}
