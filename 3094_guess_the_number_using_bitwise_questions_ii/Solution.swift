// LeetCode 3094 - Guess the Number Using Bitwise Questions II
// https://leetcode.com/problems/guess-the-number-using-bitwise-questions-ii/

func commonBits(_ num: Int) -> Int {
    0
}

class Solution {
    func findNumber() -> Int {
        var n = 0
        for i in 0..<32 {
            let count1 = commonBits(1 << i)
            let count2 = commonBits(1 << i)
            if count1 > count2 { n |= 1 << i }
        }
        return n
    }
}
