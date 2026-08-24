// LeetCode 3921 - Score Validator
// https://leetcode.com/problems/score-validator/

class Solution {
    func scoreValidator(_ events: [String]) -> [Int] {
        var score = 0, counter = 0
        for eventStr in events {
            var isNum = !eventStr.isEmpty
            var num = 0
            var start = 0
            let chars = Array(eventStr)
            if isNum && chars[0] == "-" { start = 1 }
            if start < chars.count {
                for i in start..<chars.count {
                    if chars[i] < "0" || chars[i] > "9" {
                        isNum = false
                        break
                    }
                    num = num * 10 + Int(chars[i].asciiValue! - 48)
                }
            }
            if isNum && !(start == 1 && chars.count == 1) {
                if start == 1 { num = -num }
                score += num
            } else if eventStr == "W" {
                counter += 1
                if counter == 10 { break }
            } else {
                score += 1
            }
        }
        return [score, counter]
    }
}
