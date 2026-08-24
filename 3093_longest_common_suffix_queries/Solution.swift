// LeetCode 3093 - Longest Common Suffix Queries
// https://leetcode.com/problems/longest-common-suffix-queries/

private class Trie {
    var children = [Trie?](repeating: nil, count: 26)
    var length = 1 << 30
    var idx = 1 << 30
}

class Solution {
    func stringIndices(_ wordsContainer: [String], _ wordsQuery: [String]) -> [Int] {
        let trie = Trie()
        for i in 0..<wordsContainer.count {
            insert(trie, wordsContainer[i], i)
        }
        return wordsQuery.map { query(trie, $0) }
    }

    private func insert(_ t: Trie, _ w: String, _ i: Int) {
        var node = t
        if node.length > w.count {
            node.length = w.count
            node.idx = i
        }
        let chars = Array(w)
        let a = Character("a").asciiValue!
        for k in stride(from: chars.count - 1, through: 0, by: -1) {
            let id = Int(chars[k].asciiValue! - a)
            if node.children[id] == nil { node.children[id] = Trie() }
            node = node.children[id]!
            if node.length > w.count {
                node.length = w.count
                node.idx = i
            }
        }
    }

    private func query(_ t: Trie, _ w: String) -> Int {
        var node = t
        let chars = Array(w)
        let a = Character("a").asciiValue!
        for k in stride(from: chars.count - 1, through: 0, by: -1) {
            let id = Int(chars[k].asciiValue! - a)
            guard let next = node.children[id] else { break }
            node = next
        }
        return node.idx
    }
}
