// LeetCode 3849 - Maximum Bitwise Xor After Rearrangement
// https://leetcode.com/problems/maximum-bitwise-xor-after-rearrangement/

class Solution {
    func maximumXor(_ s: String, _ t: String) -> String {
        var cnt = [0, 0]
        for c in t { cnt[Int(c.asciiValue! - 48)] += 1 }
        let sc = Array(s)
        var ans = [Character](repeating: "0", count: sc.count)
        for i in 0..<sc.count {
            let x = Int(sc[i].asciiValue! - 48)
            if cnt[x ^ 1] > 0 {
                cnt[x ^ 1] -= 1
                ans[i] = "1"
            } else {
                cnt[x] -= 1
                ans[i] = "0"
            }
        }
        return String(ans)
    }
}
