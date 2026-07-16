// LeetCode 0273 - Integer to English Words
// https://leetcode.com/problems/integer-to-english-words/

class Solution {
    private let ones = [
        "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
        "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
        "Seventeen", "Eighteen", "Nineteen",
    ]
    private let tens = [
        "", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety",
    ]
    private let thousands = ["", "Thousand", "Million", "Billion"]

    func numberToWords(_ num: Int) -> String {
        if num == 0 {
            return "Zero"
        }

        var parts: [String] = []
        var value = num
        var chunkIndex = 0
        while value > 0 {
            let chunk = value % 1000
            if chunk != 0 {
                var chunkWords = convertChunk(chunk)
                if !thousands[chunkIndex].isEmpty {
                    chunkWords += " \(thousands[chunkIndex])"
                }
                parts.append(chunkWords)
            }
            value /= 1000
            chunkIndex += 1
        }
        return parts.reversed().joined(separator: " ")
    }

    private func convertChunk(_ value: Int) -> String {
        if value == 0 {
            return ""
        }
        if value < 20 {
            return ones[value]
        }
        if value < 100 {
            let tensPart = tens[value / 10]
            let onesPart = ones[value % 10]
            return onesPart.isEmpty ? tensPart : "\(tensPart) \(onesPart)"
        }
        let hundreds = ones[value / 100]
        let remainder = convertChunk(value % 100)
        return remainder.isEmpty ? "\(hundreds) Hundred" : "\(hundreds) Hundred \(remainder)"
    }
}
