// LeetCode 0085 - Maximal Rectangle
// https://leetcode.com/problems/maximal-rectangle/

class Solution {
    func maximalRectangle(_ matrix: [[Character]]) -> Int {
        if matrix.isEmpty {
            return 0
        }

        let cols = matrix[0].count
        var heights = Array(repeating: 0, count: cols)
        var maxArea = 0

        for row in matrix {
            for j in 0..<cols {
                heights[j] = row[j] == Character("1") ? heights[j] + 1 : 0
            }
            maxArea = max(maxArea, largestHistogram(heights))
        }

        return maxArea
    }

    private func largestHistogram(_ heights: [Int]) -> Int {
        var stack = [Int]()
        var maxArea = 0
        let extended = heights + [0]

        for i in 0..<extended.count {
            let height = extended[i]
            while let top = stack.last, extended[top] > height {
                let h = extended[stack.removeLast()]
                let width = stack.isEmpty ? i : i - stack.last! - 1
                maxArea = max(maxArea, h * width)
            }
            stack.append(i)
        }

        return maxArea
    }
}
