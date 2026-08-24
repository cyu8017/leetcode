// LeetCode 3858 - Minimum Bitwise Or From Grid
// https://leetcode.com/problems/minimum-bitwise-or-from-grid/

class Solution {
    private func bitLen(_ x: Int) -> Int {
        if x == 0 { return 0 }
        var x = x, n = 0
        while x > 0 { n += 1; x >>= 1 }
        return n
    }

    func minimumOR(_ grid: [[Int]]) -> Int {
        var mx = 0
        for row in grid {
            for x in row { mx = max(mx, x) }
        }
        let m = bitLen(mx)
        var ans = 0
        if m > 0 {
            for i in stride(from: m - 1, through: 0, by: -1) {
                let mask = ans | ((1 << i) - 1)
                for row in grid {
                    var found = false
                    for x in row {
                        if (x | mask) == mask { found = true; break }
                    }
                    if !found {
                        ans |= 1 << i
                        break
                    }
                }
            }
        }
        return ans
    }
}
