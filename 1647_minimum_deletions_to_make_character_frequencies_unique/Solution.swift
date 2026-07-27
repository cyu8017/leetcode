// LeetCode 1647 - Minimum Deletions to Make Character Frequencies Unique
// https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

class Solution {
    func minDeletions(_ s: String) -> Int {
        var count = [Character: Int]()
        for ch in s { count[ch, default: 0] += 1 }
        var used = Set<Int>()
        var ans = 0
        for var x in count.values {
            while x > 0 && used.contains(x) {
                x -= 1
                ans += 1
            }
            used.insert(x)
        }
        return ans
    }
}
