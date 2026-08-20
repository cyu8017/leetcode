// LeetCode 1349 - Maximum Students Taking Exam
// https://leetcode.com/problems/maximum-students-taking-exam/

class Solution {
    func maxStudents(_ seats: [[Character]]) -> Int {
        let cols = seats[0].count
        var rowMasks = [[Int]]()
        for row in seats {
            var available = 0
            for (c, cell) in row.enumerated() where cell == "." { available |= 1 << c }
            var masks = [Int]()
            for mask in 0..<(1 << cols) {
                if mask & ~available == 0 && mask & (mask << 1) == 0 { masks.append(mask) }
            }
            rowMasks.append(masks)
        }
        var dp = [0: 0]
        for masks in rowMasks {
            var nxt = [Int: Int]()
            for mask in masks {
                for (previous, count) in dp {
                    if mask & (previous << 1) == 0 && mask & (previous >> 1) == 0 {
                        nxt[mask] = max(nxt[mask, default: 0], count + mask.nonzeroBitCount)
                    }
                }
            }
            dp = nxt
        }
        return dp.values.max() ?? 0
    }
}
