// LeetCode 2885 - Rename Columns
// https://leetcode.com/problems/rename-columns/
// Pandas stand-in.

class Solution {
    func renameColumns(_ students: [[Any]]) -> [[String: Any]] {
        return students.map { r in
            [
                "student_id": r[0],
                "first_name": r[1],
                "last_name": r[2],
                "age_in_years": r[3]
            ]
        }
    }
}
