// LeetCode 2883 - Drop Missing Data
// https://leetcode.com/problems/drop-missing-data/
// Pandas stand-in.

class Solution {
    func dropMissingData(_ students: [[Any]]) -> [[Any]] {
        return students.filter { r in
            if r.count < 2 { return false }
            if let name = r[1] as? String { return !name.isEmpty }
            return r[1] != nil
        }
    }
}
