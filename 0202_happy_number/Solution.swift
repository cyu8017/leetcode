// LeetCode 0202 - Happy Number
// https://leetcode.com/problems/happy-number/

class Solution {
    func isHappy(_ n: Int) -> Bool {
        var seen = Set<Int>()
        var number = n
        while number != 1 && !seen.contains(number) {
            seen.insert(number)
            var value = number
            var total = 0
            while value > 0 {
                let digit = value % 10
                total += digit * digit
                value /= 10
            }
            number = total
        }
        return number == 1
    }
}