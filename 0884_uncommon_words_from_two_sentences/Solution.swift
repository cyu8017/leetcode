// LeetCode 0884 - Uncommon Words from Two Sentences
// https://leetcode.com/problems/uncommon-words-from-two-sentences/

class Solution {
    func uncommonFromSentences(_ s1: String, _ s2: String) -> [String] {
        var count = [String: Int]()
        for w in (s1 + " " + s2).split(separator: " ") where !w.isEmpty {
            count[String(w), default: 0] += 1
        }
        return count.filter { $0.value == 1 }.map { $0.key }
    }
}
