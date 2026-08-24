// LeetCode 2282 - Number of People That Can Be Seen in a Grid
// https://leetcode.com/problems/number-of-people-that-can-be-seen-in-a-grid/

class Solution {
    func seePeople(_ heights: [[Int]]) -> [[Int]] {
        let m = heights.count, n = heights[0].count
        var ans = [[Int]](repeating: [Int](repeating: 0, count: n), count: m)
        for i in 0..<m {
            var stack: [Int] = []
            for j in stride(from: n - 1, through: 0, by: -1) {
                var cnt = 0
                while let last = stack.last, heights[i][last] < heights[i][j] {
                    stack.removeLast()
                    cnt += 1
                }
                if !stack.isEmpty { cnt += 1 }
                ans[i][j] += cnt
                while let last = stack.last, heights[i][last] == heights[i][j] { stack.removeLast() }
                stack.append(j)
            }
        }
        for j in 0..<n {
            var stack: [Int] = []
            for i in stride(from: m - 1, through: 0, by: -1) {
                var cnt = 0
                while let last = stack.last, heights[last][j] < heights[i][j] {
                    stack.removeLast()
                    cnt += 1
                }
                if !stack.isEmpty { cnt += 1 }
                ans[i][j] += cnt
                while let last = stack.last, heights[last][j] == heights[i][j] { stack.removeLast() }
                stack.append(i)
            }
        }
        return ans
    }
}
