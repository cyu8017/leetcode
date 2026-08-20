// LeetCode 1491 - Average Salary Excluding the Minimum and Maximum Salary
// https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

class Solution {
    func average(_ salary: [Int]) -> Double {
        Double(salary.reduce(0, +) - (salary.min()! + salary.max()!)) / Double(salary.count - 2)
    }
}
