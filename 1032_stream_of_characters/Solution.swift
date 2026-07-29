// LeetCode 1032 - Stream of Characters
// https://leetcode.com/problems/stream-of-characters/

class StreamChecker {
    private class TrieNode {
        var children = [Character: TrieNode]()
        var isWord = false
    }

    private let root = TrieNode()
    private var stream = [Character]()

    init(_ words: [String]) {
        for word in words {
            var node = root
            for ch in word.reversed() {
                if node.children[ch] == nil {
                    node.children[ch] = TrieNode()
                }
                node = node.children[ch]!
            }
            node.isWord = true
        }
    }

    func query(_ letter: Character) -> Bool {
        stream.append(letter)
        var node = root
        for ch in stream.reversed() {
            if node.isWord { return true }
            guard let next = node.children[ch] else { return false }
            node = next
        }
        return node.isWord
    }
}
