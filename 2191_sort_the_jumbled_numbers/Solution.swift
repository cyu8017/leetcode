// LeetCode 2191 - Sort the Jumbled Numbers
// https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution {
    func sortJumbled(_ mapping: [Int], _ nums: [Int]) -> [Int] {
        func mapVal(_ x: Int) -> Int {
            if x == 0 { return mapping[0] }
            var x = x
            var digits = [Int]()
            while x > 0 { digits.append(x % 10); x /= 10 }
            var res = 0
            for d in digits.reversed() { res = res * 10 + mapping[d] }
            return res
        }
        return nums.enumerated()
            .map { (mapVal($0.element), $0.offset, $0.element) }
            .sorted { $0.0 != $1.0 ? $0.0 < $1.0 : $0.1 < $1.1 }
            .map { $0.2 }
    }
}
