// LeetCode 1525 - Number of Good Ways to Split a String
// https://leetcode.com/problems/number-of-good-ways-to-split-a-string/

class Solution {
    func numSplits(_ s: String) -> Int {
        var right = [Character: Int]()
        for ch in s { right[ch, default: 0] += 1 }
        var left = Set<Character>()
        var answer = 0
        let chars = Array(s)
        for i in 0..<(chars.count - 1) {
            let ch = chars[i]
            left.insert(ch)
            right[ch]! -= 1
            if right[ch] == 0 { right.removeValue(forKey: ch) }
            if left.count == right.count { answer += 1 }
        }
        return answer
    }
}
