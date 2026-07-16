// LeetCode 0007 - Reverse Integer
// https://leetcode.com/problems/reverse-integer/

class Solution {
    func reverse(_ x: Int) -> Int {
        var value = x
        var result = 0

        while value != 0 {
            let pop = value % 10
            value /= 10

            if result > Int32.max / 10 || (result == Int32.max / 10 && pop > 7) {
                return 0
            }
            if result < Int32.min / 10 || (result == Int32.min / 10 && pop < -8) {
                return 0
            }

            result = result * 10 + pop
        }

        return result
    }
}
