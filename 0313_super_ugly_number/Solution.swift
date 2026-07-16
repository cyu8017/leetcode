// LeetCode 0313 - Super Ugly Number
// https://leetcode.com/problems/super-ugly-number/

class Solution {
    func nthSuperUglyNumber(_ n: Int, _ primes: [Int]) -> Int {
        var ugly = [1]
        var pointers = Array(repeating: 0, count: primes.count)
        while ugly.count < n {
            var nextValues = [Int]()
            for index in 0..<primes.count {
                nextValues.append(ugly[pointers[index]] * primes[index])
            }
            let nextUgly = nextValues.min()!
            ugly.append(nextUgly)
            for index in 0..<primes.count {
                if nextUgly == ugly[pointers[index]] * primes[index] {
                    pointers[index] += 1
                }
            }
        }
        return ugly[ugly.count - 1]
    }
}
