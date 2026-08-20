// LeetCode 1486 - XOR Operation in an Array
// https://leetcode.com/problems/xor-operation-in-an-array/

class Solution {
    func xorOperation(_ n: Int, _ start: Int) -> Int {
        var ans = 0
        for i in 0..<n { ans ^= start + 2 * i }
        return ans
    }
}
