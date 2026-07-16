// LeetCode 0423 - Reconstruct Original Digits from English
// https://leetcode.com/problems/reconstruct-original-digits-from-english/

class Solution {
    func originalDigits(_ s: String) -> String {
        var counts: [Character: Int] = [:]
        for char in s {
            counts[char, default: 0] += 1
        }

        var digitCounts = Array(repeating: 0, count: 10)
        digitCounts[0] = counts["z", default: 0]
        digitCounts[2] = counts["w", default: 0]
        digitCounts[4] = counts["u", default: 0]
        digitCounts[6] = counts["x", default: 0]
        digitCounts[8] = counts["g", default: 0]
        digitCounts[1] = counts["o", default: 0] - digitCounts[0] - digitCounts[2] - digitCounts[4]
        digitCounts[3] = counts["h", default: 0] - digitCounts[8]
        digitCounts[5] = counts["f", default: 0] - digitCounts[4]
        digitCounts[7] = counts["s", default: 0] - digitCounts[6]
        digitCounts[9] = counts["i", default: 0] - digitCounts[5] - digitCounts[6] - digitCounts[8]

        var result = ""
        for digit in 0..<10 {
            result += String(repeating: String(digit), count: digitCounts[digit])
        }
        return result
    }
}
