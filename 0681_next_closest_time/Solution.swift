// LeetCode 0681 - Next Closest Time
// https://leetcode.com/problems/next-closest-time/

class Solution {
    func nextClosestTime(_ time: String) -> String {
        let chars = Array(time)
        var digits = Set<Character>([chars[0], chars[1], chars[3], chars[4]])
        let start = Int(String(chars[0...1]))! * 60 + Int(String(chars[3...4]))!
        for delta in 1...(24 * 60) {
            let mins = (start + delta) % (24 * 60)
            let hh = mins / 60, mm = mins % 60
            let c0 = Character(String(hh / 10))
            let c1 = Character(String(hh % 10))
            let c2 = Character(String(mm / 10))
            let c3 = Character(String(mm % 10))
            if digits.contains(c0) && digits.contains(c1) && digits.contains(c2) && digits.contains(c3) {
                return String([c0, c1, ":", c2, c3])
            }
        }
        return time
    }
}
