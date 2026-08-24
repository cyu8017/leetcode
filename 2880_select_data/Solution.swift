// LeetCode 2880 - Select Data
// https://leetcode.com/problems/select-data/
// Pandas stand-in.

class Solution {
    func selectData(_ students: [[Any]]) -> [[String: Any]] {
        var out: [[String: Any]] = []
        for r in students {
            if let id = r[0] as? Int, id == 101 {
                out.append(["name": r[1], "age": r[2]])
            }
        }
        return out
    }
}
