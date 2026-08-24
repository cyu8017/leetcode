// LeetCode 2887 - Fill Missing Data
// https://leetcode.com/problems/fill-missing-data/
// Pandas stand-in.

class Solution {
    func fillMissingValues(_ products: [[Any]]) -> [[Any]] {
        return products.map { r in
            let q: Any = (r[1] as? Int) ?? 0
            return [r[0], q, r[2]]
        }
    }
}
