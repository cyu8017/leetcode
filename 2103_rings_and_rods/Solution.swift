// LeetCode 2103 - Rings and Rods
// https://leetcode.com/problems/rings-and-rods/

class Solution {
    func countPoints(_ rings: String) -> Int {
        let chars = Array(rings)
        var mask = [Int](repeating: 0, count: 10)
        var i = 0
        while i < chars.count {
            let c = chars[i]
            let r = Int(chars[i + 1].asciiValue! - 48)
            let bit = c == "R" ? 1 : (c == "G" ? 2 : 4)
            mask[r] |= bit
            i += 2
        }
        return mask.filter { $0 == 7 }.count
    }
}
