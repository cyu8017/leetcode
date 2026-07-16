// LeetCode 0211 - Design Add and Search Words Data Structure
// https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode {
    var children = [Character: TrieNode]()
    var isWord = false
}

class WordDictionary {
    private let root = TrieNode()

    func addWord(_ word: String) {
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
        func dfs(_ node: TrieNode, _ index: String.Index) -> Bool {
            if index == word.endIndex {
                return node.isWord
            }
            let char = word[index]
            let nextIndex = word.index(after: index)
            if char == "." {
                for child in node.children.values {
                    if dfs(child, nextIndex) {
                        return true
                    }
                }
                return false
            }
            guard let next = node.children[char] else {
                return false
            }
            return dfs(next, nextIndex)
        }
        return dfs(root, word.startIndex)
    }
}
