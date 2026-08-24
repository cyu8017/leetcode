// LeetCode 3871 - Count Commas In Range II
// https://leetcode.com/problems/count-commas-in-range-ii/

class Solution {
    func countCommas(_ n: Int) -> Int {
        var ans = 0
        var x = 1000
        while x <= n {
            ans += n - x + 1
            if x > n / 1000 { break }
            x *= 1000
        }
        return ans
    }
}
