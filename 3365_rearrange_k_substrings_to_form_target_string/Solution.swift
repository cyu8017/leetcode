// LeetCode 3365 - Rearrange K Substrings to Form Target String
// https://leetcode.com/problems/rearrange-k-substrings-to-form-target-string/

class Solution {
    func isPossibleToRearrange(_ s: String, _ t: String, _ k: Int) -> Bool {
        let sa = Array(s), ta = Array(t)
        let n = sa.count
        let sz = n / k
        var cnt = [String: Int]()
        var i = 0
        while i < n {
            let a = String(sa[i..<(i + sz)])
            let b = String(ta[i..<(i + sz)])
            cnt[a, default: 0] += 1
            cnt[b, default: 0] -= 1
            i += sz
        }
        return cnt.values.allSatisfy { $0 == 0 }
    }
}
