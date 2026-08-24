// LeetCode 2798 - Number of Employees Who Met the Target
// https://leetcode.com/problems/number-of-employees-who-met-the-target/

class Solution {
    func numberOfEmployeesWhoMetTarget(_ hours: [Int], _ target: Int) -> Int {
        hours.filter { $0 >= target }.count
    }
}
