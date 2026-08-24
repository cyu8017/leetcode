// LeetCode 2522 - Partition String Into Substrings With Values At Most K
// https://leetcode.com/problems/partition-string-into-substrings-with-values-at-most-k/

class Solution {
    func minimumPartition(_ s: String, _ k: Int) -> Int {
        var ans = 1, cur = 0
        for ch in s {
            let d = Int(ch.asciiValue! - Character("0").asciiValue!)
            if d > k { return -1 }
            let nxt = cur * 10 + d
            if nxt > k {
                ans += 1
                cur = d
            } else {
                cur = nxt
            }
        }
        return ans
    }
}
