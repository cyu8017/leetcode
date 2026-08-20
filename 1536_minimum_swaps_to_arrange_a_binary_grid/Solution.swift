// LeetCode 1536 - Minimum Swaps to Arrange a Binary Grid
// https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/

class Solution {
    func minSwaps(_ grid: [[Int]]) -> Int {
        let n = grid.count
        var zeros = [Int]()
        for row in grid {
            var count = 0
            for value in row.reversed() {
                if value != 0 { break }
                count += 1
            }
            zeros.append(count)
        }
        var answer = 0
        for i in 0..<n {
            let required = n - i - 1
            var j = i
            while j < n && zeros[j] < required { j += 1 }
            if j == n { return -1 }
            answer += j - i
            let chosen = zeros[j]
            for t in stride(from: j, through: i + 1, by: -1) {
                zeros[t] = zeros[t - 1]
            }
            zeros[i] = chosen
        }
        return answer
    }
}
