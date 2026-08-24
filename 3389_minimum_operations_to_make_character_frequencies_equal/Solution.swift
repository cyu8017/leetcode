// LeetCode 3389 - Minimum Operations to Make Character Frequencies Equal
// https://leetcode.com/problems/minimum-operations-to-make-character-frequencies-equal/

class Solution {
    func makeStringGood(_ s: String) -> Int {
        var freq = Array(repeating: 0, count: 26)
        for c in s { freq[Int(c.asciiValue! - 97)] += 1 }
        var ans = s.count
        if s.count >= 1 {
            for t in 1...s.count {
                var pool = 0, deficit = 0
                for i in 0..<26 {
                    if freq[i] > t { pool += freq[i] - t }
                    if freq[i] < t { deficit += t - freq[i] }
                }
                ans = min(ans, max(pool, deficit))
            }
        }
        return min(ans, s.count)
    }
}
