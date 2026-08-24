// LeetCode 3692 - Majority Frequency Characters
// https://leetcode.com/problems/majority-frequency-characters/

class Solution {
    func majorityFrequencyGroup(_ s: String) -> String {
        var cnt = Array(repeating: 0, count: 26)
        for c in s.utf8 { cnt[Int(c - 97)] += 1 }
        var f = [Int: String]()
        for i in 0..<26 {
            if cnt[i] > 0 {
                f[cnt[i], default: ""].append(Character(UnicodeScalar(97 + i)!))
            }
        }
        var mx = 0, mv = 0
        var ans = ""
        for (v, cs) in f {
            if cs.count > mx || (cs.count == mx && v > mv) {
                mx = cs.count
                mv = v
                ans = cs
            }
        }
        return ans
    }
}
