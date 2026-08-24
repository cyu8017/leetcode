// LeetCode 2380 - Time Needed to Rearrange a Binary String
// https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string/

class Solution {
    func secondsToRemoveOccurrences(_ s: String) -> Int {
        var ans = 0, zeros = 0
        for c in s {
            if c == "0" { zeros += 1 }
            else if zeros > 0 { ans = max(ans + 1, zeros) }
        }
        return ans
    }
}
