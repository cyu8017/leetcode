// LeetCode 1051 - Height Checker
// https://leetcode.com/problems/height-checker/

class Solution {
    func heightChecker(_ heights: [Int]) -> Int {
        let sorted = heights.sorted()
        var ans = 0
        for i in 0..<heights.count {
            if heights[i] != sorted[i] {
                ans += 1
            }
        }
        return ans
    }
}
