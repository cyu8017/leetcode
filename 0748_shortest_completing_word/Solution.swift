// LeetCode 0748 - Shortest Completing Word
// https://leetcode.com/problems/shortest-completing-word/

class Solution {
    func shortestCompletingWord(_ licensePlate: String, _ words: [String]) -> String {
        var need = Array(repeating: 0, count: 26)
        let a = Character("a").asciiValue!
        for ch in licensePlate.lowercased() where ch.isLetter {
            need[Int(ch.asciiValue! - a)] += 1
        }
        var best: String? = nil
        for word in words {
            var have = Array(repeating: 0, count: 26)
            for ch in word { have[Int(ch.asciiValue! - a)] += 1 }
            var ok = true
            for i in 0..<26 where have[i] < need[i] { ok = false }
            if ok && (best == nil || word.count < best!.count) { best = word }
        }
        return best!
    }
}
