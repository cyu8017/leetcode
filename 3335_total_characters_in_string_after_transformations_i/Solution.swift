// LeetCode 3335 - Total Characters in String After Transformations I
// https://leetcode.com/problems/total-characters-in-string-after-transformations-i/

class Solution {
    func lengthAfterTransformations(_ s: String, _ t: Int) -> Int {
        let mod = 1_000_000_007
        var cnt = Array(repeating: 0, count: 26)
        for c in s { cnt[Int(c.asciiValue! - 97)] += 1 }
        for _ in 0..<t {
            var ncnt = Array(repeating: 0, count: 26)
            for i in 0..<25 { ncnt[i + 1] = (ncnt[i + 1] + cnt[i]) % mod }
            ncnt[0] = (ncnt[0] + cnt[25]) % mod
            ncnt[1] = (ncnt[1] + cnt[25]) % mod
            cnt = ncnt
        }
        return cnt.reduce(0, +) % mod
    }
}
