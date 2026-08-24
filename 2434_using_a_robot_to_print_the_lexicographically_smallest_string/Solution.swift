// LeetCode 2434 - Using a Robot to Print the Lexicographically Smallest String
// https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/

class Solution {
    func robotWithString(_ s: String) -> String {
        let chars = Array(s)
        let n = chars.count
        var minSuf = [Character](repeating: Character("{"), count: n + 1)
        for i in stride(from: n - 1, through: 0, by: -1) {
            minSuf[i] = chars[i] < minSuf[i + 1] ? chars[i] : minSuf[i + 1]
        }
        var stack = [Character]()
        var ans = [Character]()
        for i in 0..<n {
            stack.append(chars[i])
            while !stack.isEmpty && stack.last! <= minSuf[i + 1] {
                ans.append(stack.removeLast())
            }
        }
        while !stack.isEmpty { ans.append(stack.removeLast()) }
        return String(ans)
    }
}
