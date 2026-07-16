// LeetCode 0013 - Roman to Integer
// https://leetcode.com/problems/roman-to-integer/

class Solution {
    func romanToInt(_ s: String) -> Int {
        let values: [Character: Int] = [
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000,
        ]
        var total = 0
        var prev = 0
        let chars = Array(s)

        for i in stride(from: chars.count - 1, through: 0, by: -1) {
            let curr = values[chars[i], default: 0]
            if curr < prev {
                total -= curr
            } else {
                total += curr
            }
            prev = curr
        }

        return total
    }
}
