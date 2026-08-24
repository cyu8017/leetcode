// LeetCode 3257 - Maximum Value Sum by Placing Three Rooks II
// https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-ii/

class Solution {
    func maximumValueSum(_ board: [[Int]]) -> Int {
        let m = board.count, n = board[0].count
        var tops: [[(Int, Int)]] = []
        for i in 0..<m {
            var row: [(Int, Int)] = []
            for j in 0..<n {
                let cur = (board[i][j], j)
                var placed = false
                for t in 0..<row.count where cur.0 > row[t].0 {
                    row.insert(cur, at: t)
                    placed = true
                    break
                }
                if !placed { row.append(cur) }
                if row.count > 3 { row = Array(row.prefix(3)) }
            }
            tops.append(row)
        }
        var ans = -(1 << 62)
        for i in 0..<m {
            for a in tops[i] {
                for j in (i + 1)..<m {
                    for b in tops[j] where a.1 != b.1 {
                        for k in (j + 1)..<m {
                            for c in tops[k] where c.1 != a.1 && c.1 != b.1 {
                                ans = max(ans, a.0 + b.0 + c.0)
                            }
                        }
                    }
                }
            }
        }
        return ans
    }
}
