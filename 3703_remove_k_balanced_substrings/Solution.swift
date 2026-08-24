// LeetCode 3703 - Remove K-Balanced Substrings
// https://leetcode.com/problems/remove-k-balanced-substrings/

class Solution {
    func removeSubstring(_ s: String, _ k: Int) -> String {
        var stk = [(Character, Int)]()
        for c in s {
            if let last = stk.last, last.0 == c {
                stk[stk.count - 1].1 += 1
            } else {
                stk.append((c, 1))
            }
            if c == ")" && stk.count > 1 {
                let top = stk[stk.count - 1]
                var prev = stk[stk.count - 2]
                if top.1 == k && prev.1 >= k {
                    stk.removeLast()
                    prev.1 -= k
                    if prev.1 == 0 { stk.removeLast() }
                    else { stk[stk.count - 1] = prev }
                }
            }
        }
        var res = ""
        for p in stk {
            for _ in 0..<p.1 { res.append(p.0) }
        }
        return res
    }
}
