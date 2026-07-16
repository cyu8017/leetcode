// LeetCode 0411 - Minimum Unique Word Abbreviation
// https://leetcode.com/problems/minimum-unique-word-abbreviation/

class Solution {
    private var target = ""
    private var words: [String] = []
    private var bestLen = 0
    private var result = ""

    func minAbbreviation(_ target: String, _ dictionary: [String]) -> String {
        self.target = target
        words = dictionary.filter { $0.count == target.count }
        bestLen = target.count + 1
        result = target
        dfs(0, [], 0)
        return result
    }

    private func matches(_ word: String, _ abbr: String) -> Bool {
        let wordChars = Array(word)
        let abbrChars = Array(abbr)
        var index = 0
        var pointer = 0

        while index < wordChars.count && pointer < abbrChars.count {
            if abbrChars[pointer].isNumber {
                if abbrChars[pointer] == "0" {
                    return false
                }
                var number = 0
                while pointer < abbrChars.count && abbrChars[pointer].isNumber {
                    number = number * 10 + Int(String(abbrChars[pointer]))!
                    pointer += 1
                }
                index += number
            } else {
                if wordChars[index] != abbrChars[pointer] {
                    return false
                }
                index += 1
                pointer += 1
            }
        }

        return index == wordChars.count && pointer == abbrChars.count
    }

    private func isValid(_ abbr: String) -> Bool {
        if !matches(target, abbr) {
            return false
        }
        for word in words where matches(word, abbr) {
            return false
        }
        return true
    }

    private func dfs(_ index: Int, _ parts: [String], _ skip: Int) {
        if index == target.count {
            let abbr = parts.joined() + (skip > 0 ? String(skip) : "")
            if isValid(abbr) && (abbr.count < bestLen || (abbr.count == bestLen && abbr < result)) {
                bestLen = abbr.count
                result = abbr
            }
            return
        }

        dfs(index + 1, parts, skip + 1)

        var newParts = parts
        if skip > 0 {
            newParts.append(String(skip))
        }
        let targetIndex = target.index(target.startIndex, offsetBy: index)
        newParts.append(String(target[targetIndex]))
        dfs(index + 1, newParts, 0)
    }
}
