// LeetCode 2882 - Drop Duplicate Rows
// https://leetcode.com/problems/drop-duplicate-rows/
// Pandas stand-in.

class Solution {
    func dropDuplicateEmails(_ customers: [[Any]]) -> [[Any]] {
        var seen = Set<String>()
        var out: [[Any]] = []
        for r in customers {
            let email = "\(r[2])"
            if seen.contains(email) { continue }
            seen.insert(email)
            out.append(r)
        }
        return out
    }
}
