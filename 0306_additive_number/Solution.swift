// LeetCode 0306 - Additive Number
// https://leetcode.com/problems/additive-number/

class Solution {
    func isAdditiveNumber(_ num: String) -> Bool {
        func valid(_ first: String, _ second: String, _ start: Int) -> Bool {
            if (first.count > 1 && first.first == "0") || (second.count > 1 && second.first == "0") {
                return false
            }
            var currentFirst = first
            var currentSecond = second
            var index = start
            while index < num.count {
                let total = String((Int(currentFirst) ?? 0) + (Int(currentSecond) ?? 0))
                let startIndex = num.index(num.startIndex, offsetBy: index)
                if !num[startIndex...].hasPrefix(total) {
                    return false
                }
                currentFirst = currentSecond
                currentSecond = total
                index += total.count
            }
            return true
        }

        let length = num.count
        for firstEnd in 1..<length {
            for secondEnd in (firstEnd + 1)..<length {
                let first = String(num.prefix(firstEnd))
                let secondStart = num.index(num.startIndex, offsetBy: firstEnd)
                let secondEndIndex = num.index(num.startIndex, offsetBy: secondEnd)
                let second = String(num[secondStart..<secondEndIndex])
                if valid(first, second, secondEnd) {
                    return true
                }
            }
        }
        return false
    }
}
