// LeetCode 3827 - Count Monobit Integers
// https://leetcode.com/problems/count-monobit-integers/

class Solution {
    func countMonobit(_ n: Int) -> Int {
        var ans = 1
        var i = 1, x = 1
        while x <= n {
            ans += 1
            x += (1 << i)
            i += 1
        }
        return ans
    }
}
