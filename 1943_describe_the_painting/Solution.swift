// LeetCode 1943 - Describe the Painting
// https://leetcode.com/problems/describe-the-painting/

class Solution {
    func splitPainting(_ segments: [[Int]]) -> [[Int]] {
        var diff: [Int: Int] = [:]
        for seg in segments {
            diff[seg[0], default: 0] += seg[2]
            diff[seg[1], default: 0] -= seg[2]
        }
        let points = diff.keys.sorted()
        var ans: [[Int]] = []
        var cur = 0
        for i in 0..<(points.count - 1) {
            cur += diff[points[i]]!
            if cur != 0 {
                ans.append([points[i], points[i + 1], cur])
            }
        }
        return ans
    }
}
