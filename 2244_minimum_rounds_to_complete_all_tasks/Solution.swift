// LeetCode 2244 - Minimum Rounds to Complete All Tasks
// https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/

class Solution {
    func minimumRounds(_ tasks: [Int]) -> Int {
        var freq: [Int: Int] = [:]
        for t in tasks { freq[t, default: 0] += 1 }
        var ans = 0
        for c in freq.values {
            if c == 1 { return -1 }
            ans += (c + 2) / 3
        }
        return ans
    }
}
