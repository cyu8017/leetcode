// LeetCode 3329 - Count Substrings With K-Frequency Characters II
// https://leetcode.com/problems/count-substrings-with-k-frequency-characters-ii/

class Solution {
    func numberOfSubstrings(_ s: String, _ k: Int) -> Int {
        let chars = Array(s)
        let n = chars.count
        var ans = 0
        for i in 0..<n {
            var freq = Array(repeating: 0, count: 26)
            for j in i..<n {
                freq[Int(chars[j].asciiValue! - 97)] += 1
                var ok = false
                for f in freq where f >= k { ok = true; break }
                if ok { ans += n - j; break }
            }
        }
        return ans
    }
}
