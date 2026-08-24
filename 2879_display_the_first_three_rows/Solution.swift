// LeetCode 2879 - Display the First Three Rows
// https://leetcode.com/problems/display-the-first-three-rows/
// Pandas stand-in.

class Solution {
    func selectFirstRows(_ employees: [[Any]]) -> [[Any]] {
        return Array(employees.prefix(3))
    }
}
