// LeetCode 0208 - Implement Trie (Prefix Tree)
// https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode {
    var children = [Character: TrieNode]()
    var isWord = false
}

class Trie {
    private let root = TrieNode()

    func insert(_ word: String) {
        var node = root
        for char in word {
            if node.children[char] == nil {
                node.children[char] = TrieNode()
            }
            node = node.children[char]!
        }
        node.isWord = true
    }

    func search(_ word: String) -> Bool {
        return find(word)?.isWord ?? false
    }

    func startsWith(_ prefix: String) -> Bool {
        return find(prefix) != nil
    }

    private func find(_ text: String) -> TrieNode? {
        var node = root
        for char in text {
            guard let next = node.children[char] else { return nil }
            node = next
        }
        return node
    }
}