// LeetCode 3760 - Maximum Substrings With Distinct Start
// https://leetcode.com/problems/maximum-substrings-with-distinct-start/

class Solution {
    func maxDistinct(_ s: String) -> Int {
        var cnt = [Int](repeating: 0, count: 26)
        var ans = 0
        for c in s {
            let i = Int(c.asciiValue! - 97)
            cnt[i] += 1
            if cnt[i] == 1 { ans += 1 }
        }
        return ans
    }
}
