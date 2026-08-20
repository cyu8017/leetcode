// LeetCode 1324 - Print Words Vertically
// https://leetcode.com/problems/print-words-vertically/

class Solution {
    func printVertically(_ s: String) -> [String] {
        let words = s.split(separator: " ").map(String.init)
        let width = words.map { $0.count }.max() ?? 0
        var answer = [String]()
        for i in 0..<width {
            var row = ""
            for word in words {
                let chars = Array(word)
                row.append(i < chars.count ? chars[i] : " ")
            }
            while row.last == " " { row.removeLast() }
            answer.append(row)
        }
        return answer
    }
}
