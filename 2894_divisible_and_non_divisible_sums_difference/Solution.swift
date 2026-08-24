// LeetCode 2894 - Divisible and Non-divisible Sums Difference
// https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/

class Solution {
    func differenceOfSums(_ n: Int, _ m: Int) -> Int {
        var num1 = 0, num2 = 0
        for i in 1...n {
            if i % m == 0 { num2 += i }
            else { num1 += i }
        }
        return num1 - num2
    }
}
