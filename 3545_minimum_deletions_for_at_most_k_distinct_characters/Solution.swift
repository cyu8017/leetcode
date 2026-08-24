// LeetCode 3545 - Minimum Deletions for At Most K Distinct Characters
// https://leetcode.com/problems/minimum-deletions-for-at-most-k-distinct-characters/

class Solution {
    func minDeletion(_ s: String, _ k: Int) -> Int {
        var cnt = Array(repeating: 0, count: 26)
        for c in s.utf8 { cnt[Int(c - 97)] += 1 }
        cnt.sort()
        var ans = 0
        for i in 0..<26 where i + k < 26 { ans += cnt[i] }
        return ans
    }
}
