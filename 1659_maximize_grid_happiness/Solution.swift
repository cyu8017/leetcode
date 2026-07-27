// LeetCode 1659 - Maximize Grid Happiness
// https://leetcode.com/problems/maximize-grid-happiness/

class Solution {
    func getMaxGridHappiness(_ m: Int, _ n: Int, _ introvertsCount: Int, _ extrovertsCount: Int) -> Int {
        func pair(_ a: Int, _ b: Int) -> Int {
            if a == 0 || b == 0 { return 0 }
            return (a == 1 ? -30 : 20) + (b == 1 ? -30 : 20)
        }
        var states = 1
        for _ in 0..<n { states *= 3 }
        var cells = [[Int]]()
        var intro = [Int]()
        var extro = [Int]()
        var row = [Int]()
        for s in 0..<states {
            var x = s
            var a = [Int]()
            for _ in 0..<n {
                a.append(x % 3)
                x /= 3
            }
            cells.append(a)
            intro.append(a.filter { $0 == 1 }.count)
            extro.append(a.filter { $0 == 2 }.count)
            var val = 0
            for z in a {
                if z == 1 { val += 120 }
                else if z == 2 { val += 40 }
            }
            for j in 1..<n { val += pair(a[j - 1], a[j]) }
            row.append(val)
        }
        var compat = Array(repeating: Array(repeating: 0, count: states), count: states)
        for a in 0..<states {
            for b in 0..<states {
                var s = 0
                for j in 0..<n { s += pair(cells[a][j], cells[b][j]) }
                compat[a][b] = s
            }
        }
        var memo = [Int: Int]()
        func dp(_ r: Int, _ prev: Int, _ i: Int, _ e: Int) -> Int {
            if r == m { return 0 }
            let key = (((r * states + prev) * (introvertsCount + 1) + i) * (extrovertsCount + 1)) + e
            if let v = memo[key] { return v }
            var best = 0
            for s in 0..<states {
                if intro[s] <= i && extro[s] <= e {
                    best = max(best, row[s] + compat[prev][s] + dp(r + 1, s, i - intro[s], e - extro[s]))
                }
            }
            memo[key] = best
            return best
        }
        return dp(0, 0, introvertsCount, extrovertsCount)
    }
}
