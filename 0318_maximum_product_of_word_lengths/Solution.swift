// LeetCode 0318 - Maximum Product of Word Lengths
// https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution {
    func maxProduct(_ words: [String]) -> Int {
        var masks: [Int] = []
        var lengths: [Int] = []
        for word in words {
            var mask = 0
            var valid = true
            for scalar in word.unicodeScalars {
                let bit = 1 << (Int(scalar.value) - Int(Character("a").asciiValue!))
                if mask & bit != 0 {
                    valid = false
                    break
                }
                mask |= bit
            }
            masks.append(valid ? mask : 0)
            lengths.append(word.count)
        }

        var best = 0
        for left in 0..<words.count {
            if masks[left] == 0 {
                continue
            }
            for right in (left + 1)..<words.count {
                if masks[right] == 0 {
                    continue
                }
                if masks[left] & masks[right] == 0 {
                    best = max(best, lengths[left] * lengths[right])
                }
            }
        }
        return best
    }
}
