// LeetCode 1529 - Minimum Suffix Flips
// https://leetcode.com/problems/minimum-suffix-flips/

class Solution {
    func minFlips(_ target: String) -> Int {
        let chars = Array(target)
        var ans = 0
        var prev: Character = "0"
        for ch in chars {
            if ch != prev {
                ans += 1
                prev = ch
            }
        }
        return ans
    }
}
