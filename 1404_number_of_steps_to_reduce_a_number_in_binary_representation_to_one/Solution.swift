// LeetCode 1404 - Number of Steps to Reduce a Number in Binary Representation to One
// https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/

class Solution {
    func numSteps(_ s: String) -> Int {
        let bits = Array(s)
        var steps = 0, carry = 0
        for bit in bits.dropFirst().reversed() {
            let value = Int(String(bit))! + carry
            if value == 1 { steps += 2; carry = 1 }
            else { steps += 1 }
        }
        return steps + carry
    }
}
