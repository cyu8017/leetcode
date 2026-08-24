// LeetCode 3491 - Phone Number Prefix
// https://leetcode.com/problems/phone-number-prefix/

class Solution {
    func phonePrefix(_ numbers: [String]) -> Bool {
        let numbers = numbers.sorted()
        if numbers.count >= 2 {
            for i in 0..<(numbers.count - 1) {
                if numbers[i].count <= numbers[i + 1].count && numbers[i + 1].hasPrefix(numbers[i]) {
                    return false
                }
            }
        }
        return true
    }
}
