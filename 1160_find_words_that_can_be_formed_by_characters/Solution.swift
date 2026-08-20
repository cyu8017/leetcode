// LeetCode 1160 - Find Words That Can Be Formed by Characters
// https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

class Solution {
    func countCharacters(_ words: [String], _ chars: String) -> Int {
        var avail = [Int](repeating: 0, count: 26)
        for c in chars { avail[Int(c.asciiValue! - 97)] += 1 }
        var ans = 0
        for word in words {
            var need = [Int](repeating: 0, count: 26)
            var ok = true
            for c in word {
                let idx = Int(c.asciiValue! - 97)
                need[idx] += 1
                if need[idx] > avail[idx] { ok = false; break }
            }
            if ok { ans += word.count }
        }
        return ans
    }
}
