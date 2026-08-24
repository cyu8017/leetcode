// LeetCode 2168 - Unique Substrings With Equal Digit Frequency
// https://leetcode.com/problems/unique-substrings-with-equal-digit-frequency/

class Solution {
    func equalDigitFrequency(_ s: String) -> Int {
        let chars = Array(s)
        let n = chars.count
        var seen = Set<String>()
        for i in 0..<n {
            var freq = [Int](repeating: 0, count: 10)
            var maxf = 0, kinds = 0
            for j in i..<n {
                let d = Int(chars[j].asciiValue! - 48)
                if freq[d] == 0 { kinds += 1 }
                freq[d] += 1
                maxf = max(maxf, freq[d])
                if maxf * kinds == j - i + 1 { seen.insert(String(chars[i...j])) }
            }
        }
        return seen.count
    }
}
