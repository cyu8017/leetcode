// LeetCode 1732 - Find the Highest Altitude
// https://leetcode.com/problems/find-the-highest-altitude/

class Solution {
    func largestAltitude(_ gain: [Int]) -> Int {
        var altitude = 0
        var best = 0
        for change in gain {
            altitude += change
            best = max(best, altitude)
        }
        return best
    }
}
