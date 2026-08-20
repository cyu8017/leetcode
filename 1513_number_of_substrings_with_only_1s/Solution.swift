// LeetCode 1513 - Number of Substrings With Only 1s
// https://leetcode.com/problems/number-of-substrings-with-only-1s/

class Solution {
    func numSub(_ s: String) -> Int {
        var ans = 0, run = 0
        for ch in s {
            run = ch == "1" ? run + 1 : 0
            ans += run
        }
        return ans % 1_000_000_007
    }
}
