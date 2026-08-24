// LeetCode 0660 - Remove 9
// https://leetcode.com/problems/remove-9/

class Solution {
    func newInteger(_ n: Int) -> Int {
        var n = n
        var result = 0
        var base = 1
        while n > 0 {
            result += (n % 9) * base
            n /= 9
            base *= 10
        }
        return result
    }
}
