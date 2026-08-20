// LeetCode 1178 - Number of Valid Words for Each Puzzle
// https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/

class Solution {
    func findNumOfValidWords(_ words: [String], _ puzzles: [String]) -> [Int] {
        func maskOf(_ s: String) -> Int {
            var mask = 0
            for ch in s {
                mask |= 1 << Int(ch.asciiValue! - Character("a").asciiValue!)
            }
            return mask
        }
        var freq: [Int: Int] = [:]
        for w in words {
            let m = maskOf(w)
            freq[m, default: 0] += 1
        }
        var ans: [Int] = []
        for puzzle in puzzles {
            let chars = Array(puzzle)
            let first = 1 << Int(chars[0].asciiValue! - Character("a").asciiValue!)
            let full = maskOf(puzzle)
            var sub = full
            var total = 0
            while true {
                if sub & first != 0 { total += freq[sub, default: 0] }
                if sub == 0 { break }
                sub = (sub - 1) & full
            }
            ans.append(total)
        }
        return ans
    }
}
