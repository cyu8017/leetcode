// LeetCode 3606 - Coupon Code Validator
// https://leetcode.com/problems/coupon-code-validator/

class Solution {
    func validateCoupons(_ code: [String], _ businessLine: [String], _ isActive: [Bool]) -> [String] {
        let bs: Set<String> = ["electronics", "grocery", "pharmacy", "restaurant"]
        var idx = [Int]()
        for i in 0..<code.count {
            if isActive[i] && bs.contains(businessLine[i]) && check(code[i]) { idx.append(i) }
        }
        idx.sort {
            if businessLine[$0] != businessLine[$1] { return businessLine[$0] < businessLine[$1] }
            return code[$0] < code[$1]
        }
        return idx.map { code[$0] }
    }

    func check(_ s: String) -> Bool {
        if s.isEmpty { return false }
        for c in s {
            if !(c.isLetter || c.isNumber || c == "_") { return false }
        }
        return true
    }
}
