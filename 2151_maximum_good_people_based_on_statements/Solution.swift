// LeetCode 2151 - Maximum Good People Based on Statements
// https://leetcode.com/problems/maximum-good-people-based-on-statements/

class Solution {
    func maximumGood(_ statements: [[Int]]) -> Int {
        let n = statements.count
        var ans = 0
        for mask in 0..<(1 << n) {
            if ok(statements, n, mask) { ans = max(ans, mask.nonzeroBitCount) }
        }
        return ans
    }

    private func ok(_ statements: [[Int]], _ n: Int, _ mask: Int) -> Bool {
        for i in 0..<n {
            if (mask & (1 << i)) == 0 { continue }
            for j in 0..<n {
                let s = statements[i][j]
                if s == 2 { continue }
                let goodJ = (mask & (1 << j)) != 0
                if (s == 1 && !goodJ) || (s == 0 && goodJ) { return false }
            }
        }
        return true
    }
}
