// LeetCode 2260 - Minimum Consecutive Cards to Pick Up
// https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/

class Solution {
    func minimumCardPickup(_ cards: [Int]) -> Int {
        var last: [Int: Int] = [:]
        var ans = -1
        for (i, c) in cards.enumerated() {
            if let p = last[c] {
                let diff = i - p + 1
                if ans == -1 || diff < ans { ans = diff }
            }
            last[c] = i
        }
        return ans
    }
}
