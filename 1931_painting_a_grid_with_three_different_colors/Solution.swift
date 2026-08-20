// LeetCode 1931 - Painting a Grid With Three Different Colors
// https://leetcode.com/problems/painting-a-grid-with-three-different-colors/

class Solution {
    func colorTheGrid(_ m: Int, _ n: Int) -> Int {
        let MOD = 1_000_000_007
        func validColumn(_ mask: Int) -> Bool {
            var mask = mask, prev = -1
            for _ in 0..<m {
                let c = mask % 3
                if c == prev { return false }
                prev = c
                mask /= 3
            }
            return true
        }
        func getColors(_ mask: Int) -> [Int] {
            var mask = mask, cols: [Int] = []
            for _ in 0..<m {
                cols.append(mask % 3)
                mask /= 3
            }
            return cols
        }
        var maxState = 1
        for _ in 0..<m { maxState *= 3 }
        let states = (0..<maxState).filter { validColumn($0) }
        var compat: [Int: [Int]] = [:]
        for a in states {
            let ca = getColors(a)
            compat[a] = states.filter { b in
                let cb = getColors(b)
                return zip(ca, cb).allSatisfy { $0 != $1 }
            }
        }
        var memo = [Int: Int]()
        func dp(_ col: Int, _ prev: Int) -> Int {
            if col == n { return 1 }
            let key = col * 10000 + (prev + 1)
            if let v = memo[key] { return v }
            var total = 0
            let cands = prev == -1 ? states : compat[prev]!
            for cur in cands {
                total = (total + dp(col + 1, cur)) % MOD
            }
            memo[key] = total
            return total
        }
        return dp(0, -1)
    }
}
