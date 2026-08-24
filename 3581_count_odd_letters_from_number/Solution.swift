// LeetCode 3581 - Count Odd Letters from Number
// https://leetcode.com/problems/count-odd-letters-from-number/

class Solution {
    func countOddLetters(_ n: Int) -> Int {
        let d = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        var n = n, mask = 0
        while n > 0 {
            for c in d[n % 10].utf8 { mask ^= 1 << Int(c - 97) }
            n /= 10
        }
        return mask.nonzeroBitCount
    }
}
