// LeetCode 3084 - Count Substrings Starting and Ending with Given Character
// https://leetcode.com/problems/count-substrings-starting-and-ending-with-given-character/

class Solution {
    func countSubstrings(_ s: String, _ c: Character) -> Int {
        var cnt = 0
        for ch in s where ch == c { cnt += 1 }
        return cnt * (cnt + 1) / 2
    }
}
