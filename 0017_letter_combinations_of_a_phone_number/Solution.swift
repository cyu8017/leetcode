// LeetCode 0017 - Letter Combinations of a Phone Number
// https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution {
    private let mapping = [
        "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
    ]

    func letterCombinations(_ digits: String) -> [String] {
        if digits.isEmpty {
            return []
        }

        var result: [String] = []
        var path = ""

        func backtrack(_ index: String.Index) {
            if index == digits.endIndex {
                result.append(path)
                return
            }
            let digit = digits[index]
            let letters = mapping[Int(digit.asciiValue! - 48)]
            for ch in letters {
                path.append(ch)
                backtrack(digits.index(after: index))
                path.removeLast()
            }
        }

        backtrack(digits.startIndex)
        return result
    }
}
