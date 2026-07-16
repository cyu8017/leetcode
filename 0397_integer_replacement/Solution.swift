// LeetCode 0397 - Integer Replacement
// https://leetcode.com/problems/integer-replacement/

class Solution {
    func integerReplacement(_ n: Int) -> Int {
        var value = n
        var steps = 0
        while value != 1 {
            if value % 2 == 0 {
                value /= 2
            } else if value == 3 || value % 4 == 1 {
                value -= 1
            } else {
                value += 1
            }
            steps += 1
        }
        return steps
    }
}
