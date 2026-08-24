// LeetCode 0820 - Short Encoding of Words
// https://leetcode.com/problems/short-encoding-of-words/

class Solution {
    func minimumLengthEncoding(_ words: [String]) -> Int {
        var good = Set(words)
        for word in words {
            let chars = Array(word)
            for i in 1..<chars.count {
                good.remove(String(chars[i...]))
            }
        }
        return good.reduce(0) { $0 + $1.count + 1 }
    }
}
