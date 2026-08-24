// LeetCode 2423 - Remove Letter To Equalize Frequency
// https://leetcode.com/problems/remove-letter-to-equalize-frequency/

class Solution {
    func equalFrequency(_ word: String) -> Bool {
        let chars = Array(word)
        for skip in 0..<chars.count {
            var cnt = [Int](repeating: 0, count: 26)
            for i in 0..<chars.count where i != skip {
                cnt[Int(chars[i].asciiValue! - Character("a").asciiValue!)] += 1
            }
            var freq = [Int: Int]()
            for c in cnt where c > 0 { freq[c, default: 0] += 1 }
            if freq.count == 1 { return true }
        }
        return false
    }
}
