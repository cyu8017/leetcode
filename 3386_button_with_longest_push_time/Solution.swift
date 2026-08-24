// LeetCode 3386 - Button with Longest Push Time
// https://leetcode.com/problems/button-with-longest-push-time/

class Solution {
    func buttonWithLongestTime(_ events: [[Int]]) -> Int {
        var bestT = events[0][1], bestI = events[0][0]
        for i in 1..<events.count {
            let t = events[i][1] - events[i - 1][1]
            if t > bestT || (t == bestT && events[i][0] < bestI) {
                bestT = t
                bestI = events[i][0]
            }
        }
        return bestI
    }
}
