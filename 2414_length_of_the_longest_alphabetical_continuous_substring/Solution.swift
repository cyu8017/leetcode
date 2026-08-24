// LeetCode 2414 - Length of the Longest Alphabetical Continuous Substring
// https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/

class Solution {
    func longestContinuousSubstring(_ s: String) -> Int {
        let arr = Array(s)
        var ans = 1, cur = 1
        if arr.count > 1 {
            for i in 1..<arr.count {
                if arr[i].asciiValue! == arr[i - 1].asciiValue! + 1 {
                    cur += 1
                    ans = max(ans, cur)
                } else {
                    cur = 1
                }
            }
        }
        return ans
    }
}
