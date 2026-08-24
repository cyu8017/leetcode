// LeetCode 3064 - Guess the Number Using Bitwise Questions I
// https://leetcode.com/problems/guess-the-number-using-bitwise-questions-i/

func commonSetBits(_ num: Int) -> Int {
    0
}

class Solution {
    func findNumber() -> Int {
        var n = 0
        for i in 0..<32 {
            if commonSetBits(1 << i) > 0 {
                n |= 1 << i
            }
        }
        return n
    }
}
