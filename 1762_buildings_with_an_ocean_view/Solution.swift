// LeetCode 1762 - Buildings With an Ocean View
// https://leetcode.com/problems/buildings-with-an-ocean-view/

class Solution {
    func findBuildings(_ heights: [Int]) -> [Int] {
        var ans = [Int]()
        var tallest = 0
        for i in stride(from: heights.count - 1, through: 0, by: -1) {
            if heights[i] > tallest {
                ans.append(i)
                tallest = heights[i]
            }
        }
        return ans.reversed()
    }
}
