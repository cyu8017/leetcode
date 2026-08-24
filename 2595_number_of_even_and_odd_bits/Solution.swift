// LeetCode 2595 - Number of Even and Odd Bits
// https://leetcode.com/problems/number-of-even-and-odd-bits/

class Solution {
    func evenOddBit(_ n: Int) -> [Int] {
        var n = n, even = 0, odd = 0, i = 0
        while n > 0 {
            if n & 1 != 0 {
                if i % 2 == 0 { even += 1 } else { odd += 1 }
            }
            i += 1
            n >>= 1
        }
        return [even, odd]
    }
}
