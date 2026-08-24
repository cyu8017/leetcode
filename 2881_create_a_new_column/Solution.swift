// LeetCode 2881 - Create a New Column
// https://leetcode.com/problems/create-a-new-column/
// Pandas stand-in.

class Solution {
    func createBonusColumn(_ employees: [[Any]]) -> [[String: Any]] {
        return employees.map { r in
            let salary = r[1] as? Int ?? 0
            return ["name": r[0], "salary": salary, "bonus": salary * 2]
        }
    }
}
