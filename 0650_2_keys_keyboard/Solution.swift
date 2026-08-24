// LeetCode 0650 - 2 Keys Keyboard
// https://leetcode.com/problems/2-keys-keyboard/

class Solution {
    func minSteps(_ n: Int) -> Int {
        var n = n
        var steps = 0
        var factor = 2
        while factor * factor <= n {
            while n % factor == 0 {
                steps += factor
                n /= factor
            }
            factor += 1
        }
        if n > 1 { steps += n }
        return steps
    }
}
