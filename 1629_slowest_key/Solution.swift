// LeetCode 1629 - Slowest Key
// https://leetcode.com/problems/slowest-key/

class Solution {
    func slowestKey(_ releaseTimes: [Int], _ keysPressed: String) -> Character {
        let keys = Array(keysPressed)
        var bestDuration = releaseTimes[0]
        var bestKey = keys[0]
        for i in 1..<releaseTimes.count {
            let duration = releaseTimes[i] - releaseTimes[i - 1]
            if duration > bestDuration || (duration == bestDuration && keys[i] > bestKey) {
                bestDuration = duration
                bestKey = keys[i]
            }
        }
        return bestKey
    }
}
