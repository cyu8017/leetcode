// LeetCode 1804 - Implement Trie II (Prefix Tree)
// https://leetcode.com/problems/implement-trie-ii-prefix-tree/

private class TrieIINode {
    var children = [Character: TrieIINode]()
    var wordCount = 0
    var prefixCount = 0
}

class Trie {
    private let root = TrieIINode()

    func insert(_ word: String) {
        var node = root
        for ch in word {
            if node.children[ch] == nil {
                node.children[ch] = TrieIINode()
            }
            node = node.children[ch]!
            node.prefixCount += 1
        }
        node.wordCount += 1
    }

    func countWordsEqualTo(_ word: String) -> Int {
        return find(word)?.wordCount ?? 0
    }

    func countWordsStartingWith(_ prefix: String) -> Int {
        return find(prefix)?.prefixCount ?? 0
    }

    func erase(_ word: String) {
        var node = root
        for ch in word {
            node = node.children[ch]!
            node.prefixCount -= 1
        }
        node.wordCount -= 1
    }

    private func find(_ text: String) -> TrieIINode? {
        var node = root
        for ch in text {
            guard let next = node.children[ch] else { return nil }
            node = next
        }
        return node
    }
}
