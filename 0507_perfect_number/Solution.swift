// LeetCode 0507 - Perfect Number
// https://leetcode.com/problems/perfect-number/

class Solution {
    func checkPerfectNumber(_ num: Int) -> Bool {
        if num <= 1 {
            return false
        }
        var total = 1
        let limit = Int(Double(num).squareRoot())
        if limit >= 2 {
            for divisor in 2...limit {
                if num % divisor == 0 {
                    total += divisor
                    let pair = num / divisor
                    if pair != divisor {
                        total += pair
                    }
                }
            }
        }
        return total == num
    }
}
