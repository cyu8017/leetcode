// LeetCode 0418 - Sentence Screen Fitting
// https://leetcode.com/problems/sentence-screen-fitting/

class Solution {
    func wordsTyping(_ sentence: [String], _ rows: Int, _ cols: Int) -> Int {
        var count = 0
        var index = 0
        let total = sentence.count

        for _ in 0..<rows {
            var col = 0
            while true {
                let word = sentence[index]
                let needed = word.count + (col > 0 ? 1 : 0)
                if col + needed > cols {
                    break
                }
                if col > 0 {
                    col += 1
                }
                col += word.count
                index = (index + 1) % total
                if index == 0 {
                    count += 1
                }
            }
        }

        return count
    }
}
