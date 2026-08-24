// LeetCode 0950 - Reveal Cards In Increasing Order
// https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution {
    func deckRevealedIncreasing(_ deck: [Int]) -> [Int] {
        let cards = deck.sorted()
        var idx = Array(0..<deck.count)
        var ans = Array(repeating: 0, count: deck.count)
        for card in cards {
            ans[idx.removeFirst()] = card
            if !idx.isEmpty { idx.append(idx.removeFirst()) }
        }
        return ans
    }
}
