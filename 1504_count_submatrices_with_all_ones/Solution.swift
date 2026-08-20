// LeetCode 1504 - Count Submatrices With All Ones
// https://leetcode.com/problems/count-submatrices-with-all-ones/

class Solution {
    func numSubmat(_ mat: [[Int]]) -> Int {
        var ans = 0
        var heights = Array(repeating: 0, count: mat[0].count)
        for row in mat {
            for j in 0..<row.count {
                heights[j] = row[j] == 0 ? 0 : heights[j] + 1
            }
            var stack = [(Int, Int)]()
            var running = 0
            for h in heights {
                var count = 1
                while let last = stack.last, last.0 >= h {
                    let (old, width) = stack.removeLast()
                    running -= old * width
                    count += width
                }
                stack.append((h, count))
                running += h * count
                ans += running
            }
        }
        return ans
    }
}
