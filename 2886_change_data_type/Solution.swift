// LeetCode 2886 - Change Data Type
// https://leetcode.com/problems/change-data-type/
// Pandas stand-in.

class Solution {
    func changeDatatype(_ students: [[Any]]) -> [[Any]] {
        return students.map { r in
            var grade = 0
            if let g = r[3] as? Int { grade = g }
            else if let g = r[3] as? Double { grade = Int(g) }
            return [r[0], r[1], r[2], grade]
        }
    }
}
