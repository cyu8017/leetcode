// LeetCode 0068 - Text Justification
// https://leetcode.com/problems/text-justification/

class Solution {
    func fullJustify(_ words: [String], _ maxWidth: Int) -> [String] {
        var result: [String] = []
        var i = 0

        while i < words.count {
            var lineWords: [String] = []
            var lineLen = 0

            while i < words.count {
                let word = words[i]
                let extra = lineWords.isEmpty ? 0 : 1
                if lineLen + word.count + extra > maxWidth {
                    break
                }
                lineWords.append(word)
                lineLen += word.count + extra
                i += 1
            }

            if i == words.count || lineWords.count == 1 {
                var line = lineWords.joined(separator: " ")
                line += String(repeating: " ", count: maxWidth - line.count)
                result.append(line)
            } else {
                let totalChars = lineWords.reduce(0) { $0 + $1.count }
                let totalSpaces = maxWidth - totalChars
                let gaps = lineWords.count - 1
                let space = totalSpaces / gaps
                let remainder = totalSpaces % gaps
                var line = ""
                for j in 0..<(lineWords.count - 1) {
                    line += lineWords[j]
                    line += String(repeating: " ", count: space + (j < remainder ? 1 : 0))
                }
                line += lineWords.last!
                result.append(line)
            }
        }

        return result
    }
}
