// LeetCode 1698 - Number of Distinct Substrings in a String
// https://leetcode.com/problems/number-of-distinct-substrings-in-a-string/

class Solution {
    func countDistinct(_ s: String) -> Int {
        class TrieNode {
            var children = [Character: TrieNode]()
        }
        let root = TrieNode()
        var ans = 0
        let chars = Array(s)
        for i in 0..<chars.count {
            var node = root
            for j in i..<chars.count {
                let c = chars[j]
                if node.children[c] == nil {
                    node.children[c] = TrieNode()
                    ans += 1
                }
                node = node.children[c]!
            }
        }
        return ans
    }
}
