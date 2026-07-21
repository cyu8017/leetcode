// LeetCode 1835 - Find XOR Sum of All Pairs Bitwise AND
// https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and/

class Solution {
    func getXORSum(_ arr1: [Int], _ arr2: [Int]) -> Int {
        let xor1 = arr1.reduce(0, ^)
        let xor2 = arr2.reduce(0, ^)
        return xor1 & xor2
    }
}
