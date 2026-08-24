// LeetCode 0755 - Pour Water
// https://leetcode.com/problems/pour-water/

class Solution {
    func pourWater(_ heights: [Int], _ volume: Int, _ k: Int) -> [Int] {
        var heights = heights
        for _ in 0..<volume {
            var index = k
            for i in stride(from: k - 1, through: 0, by: -1) {
                if heights[i] > heights[index] { break }
                if heights[i] < heights[index] { index = i }
            }
            if index != k { heights[index] += 1; continue }
            index = k
            for i in (k + 1)..<heights.count {
                if heights[i] > heights[index] { break }
                if heights[i] < heights[index] { index = i }
            }
            heights[index] += 1
        }
        return heights
    }
}
