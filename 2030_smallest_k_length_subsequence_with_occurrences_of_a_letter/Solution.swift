// LeetCode 2030 - Smallest K-Length Subsequence With Occurrences of a Letter
// https://leetcode.com/problems/smallest-k-length-subsequence-with-occurrences-of-a-letter/

class Solution {
    func smallestSubsequence(_ s: String, _ k: Int, _ letter: Character, _ repetition: Int) -> String {
        let chars = Array(s)
        let n = chars.count
        var remainLetter = chars.filter { $0 == letter }.count
        var stack = [Character]()
        var inStackLetter = 0
        for i in 0..<n {
            let ch = chars[i]
            while !stack.isEmpty && ch < stack.last! && stack.count + n - i > k {
                let top = stack.last!
                if top == letter {
                    if inStackLetter + remainLetter - 1 < repetition { break }
                    inStackLetter -= 1
                }
                stack.removeLast()
            }
            if stack.count < k {
                if ch == letter {
                    stack.append(ch)
                    inStackLetter += 1
                } else if k - stack.count > repetition - inStackLetter {
                    stack.append(ch)
                }
            }
            if ch == letter { remainLetter -= 1 }
        }
        return String(stack)
    }
}
