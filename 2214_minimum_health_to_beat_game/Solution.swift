// LeetCode 2214 - Minimum Health to Beat Game
// https://leetcode.com/problems/minimum-health-to-beat-game/

class Solution {
    func minimumHealth(_ damage: [Int], _ armor: Int) -> Int {
        var sum = 0
        var mx = 0
        for d in damage {
            sum += d
            mx = max(mx, d)
        }
        return sum - min(armor, mx) + 1
    }
}
