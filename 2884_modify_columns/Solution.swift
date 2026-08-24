// LeetCode 2884 - Modify Columns
// https://leetcode.com/problems/modify-columns/
// Pandas stand-in.

class Solution {
    func modifySalaryColumn(_ employees: [[Any]]) -> [[Any]] {
        return employees.map { r in
            let salary = r[1] as? Int ?? 0
            return [r[0], salary * 2]
        }
    }
}
