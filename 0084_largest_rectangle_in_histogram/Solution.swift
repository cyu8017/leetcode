// LeetCode 0084 - Largest Rectangle in Histogram
// https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution {
    func largestRectangleArea(_ heights: [Int]) -> Int {
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
