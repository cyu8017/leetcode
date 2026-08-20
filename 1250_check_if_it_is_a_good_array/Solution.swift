// LeetCode 1250 - Check If It Is a Good Array
// https://leetcode.com/problems/check-if-it-is-a-good-array/

class Solution {
    func isGoodArray(_ nums: [Int]) -> Bool {
        func gcd(_ a: Int, _ b: Int) -> Int {
            var a = a, b = b
            while b != 0 { let t = b; b = a % b; a = t }
            return a
        }
        return nums.reduce(0, gcd) == 1
    }
}
