// LeetCode 1848 - Minimum Distance to the Target Element
// https://leetcode.com/problems/minimum-distance-to-the-target-element/

class Solution {
    func getMinDistance(_ nums: [Int], _ target: Int, _ start: Int) -> Int {
        var best = nums.count
        for (i, value) in nums.enumerated() where value == target {
            best = min(best, abs(i - start))
        }
        return best
    }
}
