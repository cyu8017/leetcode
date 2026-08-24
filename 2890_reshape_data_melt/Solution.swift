// LeetCode 2890 - Reshape Data: Melt
// https://leetcode.com/problems/reshape-data-melt/
// Pandas stand-in.

class Solution {
    func meltTable(_ report: [[Any]]) -> [[String: Any]] {
        var out: [[String: Any]] = []
        for r in report {
            let product = r[0]
            for q in 1...4 {
                out.append(["product": product, "quarter": "quarter_\(q)", "sales": r[q]])
            }
        }
        return out
    }
}
