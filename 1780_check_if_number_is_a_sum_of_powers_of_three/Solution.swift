// LeetCode 1780 - Check if Number is a Sum of Powers of Three
// https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/

class Solution {
    func checkPowersOfThree(_ n: Int) -> Bool {
        var value = n
        while value > 0 {
            if value % 3 == 2 {
                return false
            }
            value /= 3
        }
        return true
    }
}
