// LeetCode 2268 - Minimum Number of Keypresses
// https://leetcode.com/problems/minimum-number-of-keypresses/

class Solution {
    func minimumKeypresses(_ s: String) -> Int {
        var freq = [Int](repeating: 0, count: 26)
        for ch in s.utf8 { freq[Int(ch - 97)] += 1 }
        freq.sort(by: >)
        var ans = 0
        for i in 0..<26 {
            if freq[i] == 0 { break }
            ans += freq[i] * (i / 9 + 1)
        }
        return ans
    }
}
