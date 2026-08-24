// LeetCode 3417 - Zigzag Grid Traversal With Skip
// https://leetcode.com/problems/zigzag-grid-traversal-with-skip/

class Solution {
    func zigzagTraversal(_ grid: [[Int]]) -> [Int] {
        var ans = [Int]()
        var skip = false
        for i in 0..<grid.count {
            let row = grid[i]
            if i % 2 == 0 {
                for v in row {
                    if !skip { ans.append(v) }
                    skip = !skip
                }
            } else {
                for j in stride(from: row.count - 1, through: 0, by: -1) {
                    if !skip { ans.append(row[j]) }
                    skip = !skip
                }
            }
        }
        return ans
    }
}
