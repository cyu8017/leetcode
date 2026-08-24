// LeetCode 0762 - Prime Number of Set Bits in Binary Representation
// https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/

class Solution {
    func countPrimeSetBits(_ left: Int, _ right: Int) -> Int {
        let primes: Set<Int> = [2, 3, 5, 7, 11, 13, 17, 19]
        return (left...right).filter { primes.contains($0.nonzeroBitCount) }.count
    }
}
