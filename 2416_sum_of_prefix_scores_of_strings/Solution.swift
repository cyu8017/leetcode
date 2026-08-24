// LeetCode 2416 - Sum of Prefix Scores of Strings
// https://leetcode.com/problems/sum-of-prefix-scores-of-strings/

class Solution {
    func sumPrefixScores(_ words: [String]) -> [Int] {
        class TrieNode {
            var child = [TrieNode?](repeating: nil, count: 26)
            var cnt = 0
        }
        let root = TrieNode()
        for w in words {
            var cur = root
            for ch in w {
                let c = Int(ch.asciiValue! - Character("a").asciiValue!)
                if cur.child[c] == nil { cur.child[c] = TrieNode() }
                cur = cur.child[c]!
                cur.cnt += 1
            }
        }
        var ans = [Int](repeating: 0, count: words.count)
        for i in 0..<words.count {
            var cur = root
            var sum = 0
            for ch in words[i] {
                let c = Int(ch.asciiValue! - Character("a").asciiValue!)
                cur = cur.child[c]!
                sum += cur.cnt
            }
            ans[i] = sum
        }
        return ans
    }
}
