// LeetCode 1781 - Sum of Beauty of All Substrings
// https://leetcode.com/problems/sum-of-beauty-of-all-substrings/

class Solution {
    func beautySum(_ s: String) -> Int {
        let chars = Array(s.utf8)
        let aValue = Int(UInt8(ascii: "a"))
        var ans = 0
        for i in 0..<chars.count {
            var freq = [Int](repeating: 0, count: 26)
            for j in i..<chars.count {
                freq[Int(chars[j]) - aValue] += 1
                var lo = Int.max
                var hi = 0
                for count in freq where count > 0 {
                    lo = min(lo, count)
                    hi = max(hi, count)
                }
                ans += hi - lo
            }
        }
        return ans
    }
}
