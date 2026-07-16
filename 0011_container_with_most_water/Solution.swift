// LeetCode 0011 - Container With Most Water
// https://leetcode.com/problems/container-with-most-water/

class Solution {
    func maxArea(_ height: [Int]) -> Int {
        var left = 0
        var right = height.count - 1
        var best = 0

        while left < right {
            let width = right - left
            best = max(best, min(height[left], height[right]) * width)
            if height[left] < height[right] {
                left += 1
            } else {
                right -= 1
            }
        }

        return best
    }
}
