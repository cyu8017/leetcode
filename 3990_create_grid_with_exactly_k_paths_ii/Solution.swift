// LeetCode 3990 - Create Grid With Exactly K Paths II
// https://leetcode.com/problems/create-grid-with-exactly-k-paths-ii/


class Solution {
    func createGrid(_ k: Int) -> [String] {
        if k <= 0 { return [] }
        func bitWidth(_ k0: Int) -> Int {
            var w = 0, k = k0
            while k != 0 { w += 1; k >>= 1 }
            return w
        }
        let l = bitWidth(k)
        let m = 2 * l, n = l + 3
        var result = Array(repeating: String(repeating: "#", count: n), count: m)
        for i in 0..<l {
            let r = 2 * i
            var row0 = Array(result[r])
            var row1 = Array(result[r + 1])
            row0[i] = "."
            row0[i + 1] = "."
            row1[i] = "."
            row1[i + 1] = "."
            if (k & (1 << i)) != 0 {
                for c in (i + 2)..<n { row0[c] = "." }
            }
            result[r] = String(row0)
            result[r + 1] = String(row1)
        }
        for r in 0..<m {
            var row = Array(result[r])
            row[n - 1] = "."
            result[r] = String(row)
        }
        return result
    }
}
