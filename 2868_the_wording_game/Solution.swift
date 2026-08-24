// LeetCode 2868 - The Wording Game
// https://leetcode.com/problems/the-wording-game/

class Solution {
    func canAliceWin(_ a: [String], _ b: [String]) -> Bool {
        var i = 0, j = 0
        var last: Character = "\u{0}"
        var alice = true
        while true {
            if alice {
                while i < a.count && a[i].first! <= last { i += 1 }
                if i == a.count { return false }
                last = a[i].last!
                i += 1
            } else {
                while j < b.count && b[j].first! <= last { j += 1 }
                if j == b.count { return true }
                last = b[j].last!
                j += 1
            }
            alice.toggle()
        }
    }
}
