// LeetCode 2683 - Neighboring XOR
// https://leetcode.com/problems/neighboring-bitwise-xor/

class Solution {
    func doesValidArrayExist(_ derived: [Int]) -> Bool {
        derived.reduce(0, ^) == 0
    }
}
