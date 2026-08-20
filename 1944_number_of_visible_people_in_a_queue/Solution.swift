// LeetCode 1944 - Number of Visible People in a Queue
// https://leetcode.com/problems/number-of-visible-people-in-a-queue/

class Solution {
    func canSeePersonsCount(_ heights: [Int]) -> [Int] {
        let n = heights.count
        var ans = Array(repeating: 0, count: n)
        var stack: [Int] = []
        for i in stride(from: n - 1, through: 0, by: -1) {
            var count = 0
            while !stack.isEmpty && heights[i] > stack.last! {
                stack.removeLast()
                count += 1
            }
            if !stack.isEmpty { count += 1 }
            ans[i] = count
            stack.append(heights[i])
        }
        return ans
    }
}
