// LeetCode 0953 - Verifying an Alien Dictionary
// https://leetcode.com/problems/verifying-an-alien-dictionary/

class Solution {
    func isAlienSorted(_ words: [String], _ order: String) -> Bool {
        var rank = Array(repeating: 0, count: 26)
        let a = Int(Character("a").asciiValue!)
        for (i, ch) in order.enumerated() { rank[Int(ch.asciiValue!) - a] = i }
        func lessEq(_ aS: String, _ bS: String) -> Bool {
            let ca = Array(aS), cb = Array(bS)
            let n = min(ca.count, cb.count)
            for i in 0..<n {
                let ra = rank[Int(ca[i].asciiValue!) - a]
                let rb = rank[Int(cb[i].asciiValue!) - a]
                if ra != rb { return ra < rb }
            }
            return ca.count <= cb.count
        }
        for i in 0..<(words.count - 1) {
            if !lessEq(words[i], words[i + 1]) { return false }
        }
        return true
    }
}
