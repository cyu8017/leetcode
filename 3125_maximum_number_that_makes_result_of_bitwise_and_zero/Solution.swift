// LeetCode 3125 - Maximum Number That Makes Result of Bitwise AND Zero
// https://leetcode.com/problems/maximum-number-that-makes-result-of-bitwise-and-zero/

class Solution {
    func maxNumber(_ n: Int) -> Int {
        let len = n.bitWidth - n.leadingZeroBitCount
        return (1 << (len - 1)) - 1
    }
}
