// LeetCode 0371 - Sum of Two Integers
// https://leetcode.com/problems/sum-of-two-integers/

class Solution {
    func getSum(_ a: Int, _ b: Int) -> Int {
        var x = a
        var y = b
        let mask = 0xFFFFFFFF

        while y != 0 {
            let carry = (x & y) << 1
            x = (x ^ y) & mask
            y = carry & mask
        }

        return x <= 0x7FFFFFFF ? x : ~(x ^ mask)
    }
}
