// LeetCode 2515 - Shortest Distance to Target String in a Circular Array
// https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/

class Solution {
    func closestTarget(_ words: [String], _ target: String, _ startIndex: Int) -> Int {
        let n = words.count
        var best = -1
        for i in 0..<n where words[i] == target {
            var d = abs(i - startIndex)
            d = min(d, n - d)
            if best < 0 || d < best { best = d }
        }
        return best
    }
}
