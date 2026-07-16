// LeetCode 0365 - Water and Jug Problem
// https://leetcode.com/problems/water-and-jug-problem/

class Solution {
    func canMeasureWater(_ x: Int, _ y: Int, _ target: Int) -> Bool {
        if target == 0 {
            return true
        }
        if x + y < target {
            return false
        }
        return target % gcd(x, y) == 0
    }

    private func gcd(_ a: Int, _ b: Int) -> Int {
        var a = a
        var b = b
        while b != 0 {
            let remainder = a % b
            a = b
            b = remainder
        }
        return a
    }
}
