// LeetCode 2347 - Best Poker Hand
// https://leetcode.com/problems/best-poker-hand/

class Solution {
    func bestHand(_ ranks: [Int], _ suits: [Character]) -> String {
        if suits[0] == suits[1] && suits[1] == suits[2] && suits[2] == suits[3] && suits[3] == suits[4] {
            return "Flush"
        }
        var cnt: [Int: Int] = [:]
        var best = 0
        for r in ranks {
            cnt[r, default: 0] += 1
            best = max(best, cnt[r]!)
        }
        if best >= 3 { return "Three of a Kind" }
        if best == 2 { return "Pair" }
        return "High Card"
    }
}
