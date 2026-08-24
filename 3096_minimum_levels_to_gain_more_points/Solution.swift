// LeetCode 3096 - Minimum Levels to Gain More Points
// https://leetcode.com/problems/minimum-levels-to-gain-more-points/

class Solution {
    func minimumLevels(_ possible: [Int]) -> Int {
        var s = 0
        for x in possible { s += x == 0 ? -1 : x }
        var t = 0
        for i in 0..<(possible.count - 1) {
            t += possible[i] == 0 ? -1 : possible[i]
            if t > s - t { return i + 1 }
        }
        return -1
    }
}
