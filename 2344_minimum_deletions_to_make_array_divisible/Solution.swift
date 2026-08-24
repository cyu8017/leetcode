// LeetCode 2344 - Minimum Deletions to Make Array Divisible
// https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/

class Solution {
    func minOperations(_ nums: [Int], _ numsDivide: [Int]) -> Int {
        func gcd(_ a: Int, _ b: Int) -> Int {
            var a = a, b = b
            while b != 0 { let t = a % b; a = b; b = t }
            return a
        }
        var g = numsDivide[0]
        for i in 1..<numsDivide.count { g = gcd(g, numsDivide[i]) }
        for (i, x) in nums.sorted().enumerated() {
            if g % x == 0 { return i }
        }
        return -1
    }
}
