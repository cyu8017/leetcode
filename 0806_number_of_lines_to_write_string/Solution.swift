// LeetCode 0806 - Number of Lines To Write String
// https://leetcode.com/problems/number-of-lines-to-write-string/

class Solution {
    func numberOfLines(_ widths: [Int], _ s: String) -> [Int] {
        var lines = 1, width = 0
        let a = Int(Character("a").asciiValue!)
        for ch in s {
            let w = widths[Int(ch.asciiValue!) - a]
            if width + w > 100 {
                lines += 1
                width = w
            } else {
                width += w
            }
        }
        return [lines, width]
    }
}
