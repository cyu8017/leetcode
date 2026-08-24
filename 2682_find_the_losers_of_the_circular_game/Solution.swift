// LeetCode 2682 - Find the Losers of the Circular Game
// https://leetcode.com/problems/find-the-losers-of-the-circular-game/

class Solution {
    func circularGameLosers(_ n: Int, _ k: Int) -> [Int] {
        var seen = Array(repeating: false, count: n + 1)
        var cur = 1
        var step = 1
        while !seen[cur] {
            seen[cur] = true
            cur = (cur - 1 + step * k) % n + 1
            step += 1
        }
        var ans: [Int] = []
        for i in 1...n where !seen[i] { ans.append(i) }
        return ans
    }
}
