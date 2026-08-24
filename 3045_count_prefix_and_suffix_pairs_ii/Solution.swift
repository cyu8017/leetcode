// LeetCode 3045 - Count Prefix and Suffix Pairs II
// https://leetcode.com/problems/count-prefix-and-suffix-pairs-ii/

class Solution {
    private class Node {
        var children: [Int: Node] = [:]
        var cnt = 0
    }

    func countPrefixSuffixPairs(_ words: [String]) -> Int {
        let trie = Node()
        var ans = 0
        for s in words {
            var node = trie
            let chars = Array(s)
            let m = chars.count
            for i in 0..<m {
                let p = Int(chars[i].asciiValue!) * 32 + Int(chars[m - i - 1].asciiValue!)
                if node.children[p] == nil { node.children[p] = Node() }
                node = node.children[p]!
                ans += node.cnt
            }
            node.cnt += 1
        }
        return ans
    }
}
