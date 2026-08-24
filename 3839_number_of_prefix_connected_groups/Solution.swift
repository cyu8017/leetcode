// LeetCode 3839 - Number Of Prefix Connected Groups
// https://leetcode.com/problems/number-of-prefix-connected-groups/

class Solution {
    func prefixConnected(_ words: [String], _ k: Int) -> Int {
        var cnt = [String: Int]()
        for w in words {
            if w.count >= k {
                let p = String(w.prefix(k))
                cnt[p, default: 0] += 1
            }
        }
        var ans = 0
        for v in cnt.values where v > 1 { ans += 1 }
        return ans
    }
}
