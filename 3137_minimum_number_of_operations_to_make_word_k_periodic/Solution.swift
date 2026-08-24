// LeetCode 3137 - Minimum Number of Operations to Make Word K-Periodic
// https://leetcode.com/problems/minimum-number-of-operations-to-make-word-k-periodic/

class Solution {
    func minimumOperationsToMakeKPeriodic(_ word: String, _ k: Int) -> Int {
        let chars = Array(word)
        var cnt: [String: Int] = [:]
        var mx = 0
        var i = 0
        while i < chars.count {
            let s = String(chars[i..<(i + k)])
            cnt[s, default: 0] += 1
            mx = max(mx, cnt[s]!)
            i += k
        }
        return chars.count / k - mx
    }
}
